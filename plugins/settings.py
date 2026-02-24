from aiogram import Router, types, F, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.exceptions import TelegramBadRequest
from config import CHANNEL_URL, DEV_URL
from database import get_thumbnail, set_thumbnail, remove_thumbnail, is_banned
router = Router()

def small_caps(text: str) -> str:
    """Convert text to small caps unicode."""
    normal = "abcdefghijklmnopqrstuvwxyz"
    small = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    result = ""
    for char in text:
        if char.lower() in normal:
            idx = normal.index(char.lower())
            result += small[idx]
        else:
            result += char
    return result

class ThumbnailState(StatesGroup):
    waiting_for_thumbnail = State()
def get_settings_keyboard():
    """Return the settings inline keyboard."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🖼️ Update Thumbnail", callback_data="update_thumb")],
        [InlineKeyboardButton(text="👁️ View Thumbnail", callback_data="view_thumb")],
        [InlineKeyboardButton(text="🗑️ Remove Thumbnail", callback_data="remove_thumb")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="back_to_start")],
        [InlineKeyboardButton(text="❌ Close", callback_data="close_settings")]
    ])

@router.callback_query(F.data == "settings")
async def show_settings(callback: CallbackQuery, bot: Bot):
    """Show settings menu - fast text only."""
    user_id = callback.from_user.id
    
    if await is_banned(user_id):
        await callback.answer(small_caps("You are banned!"), show_alert=True)
        return
    
    thumb = await get_thumbnail(user_id)
    status = f"✅ {small_caps('Thumbnail is set')}" if thumb else f"❌ {small_caps('No thumbnail set')}"
    
    text = (
        f"<b>⚙️ {small_caps('Thumbnail Settings')}</b>\n\n"
        f"<blockquote>{status}</blockquote>\n\n"
        f"{small_caps('Choose an option below:')}"
    )
    
    # Delete old message and send new one (fast, no image)
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
    
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=text,
        parse_mode="HTML",
        reply_markup=get_settings_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery, bot: Bot):
    """Go back to start message - fast text only."""
    
    welcome_text = (
        f"<b>{small_caps('Welcome to Thumbnail Bot!')}</b>\n\n"
        f"<blockquote>{small_caps('Send me a video and I will add your custom thumbnail to it.')}</blockquote>\n\n"
        f"<b>{small_caps('How to use:')}</b>\n"
        f"<blockquote>"
        f"1️ {small_caps('Set your thumbnail in Settings')}\n"
        f"2️ {small_caps('Send any video')}\n"
        f"3️ {small_caps('Get video with your thumbnail!')}"
        f"</blockquote>"
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📢 Join Channel", url=CHANNEL_URL),
            InlineKeyboardButton(text="👨‍💻 Developer", url=DEV_URL)
        ],
        [InlineKeyboardButton(text="⚙️ Settings", callback_data="settings")]
    ])
    
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
    
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=welcome_text,
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await callback.answer()

@router.callback_query(F.data == "update_thumb")
async def update_thumbnail_prompt(callback: CallbackQuery, state: FSMContext, bot: Bot):
    """Prompt user to send a new thumbnail."""
    user_id = callback.from_user.id
    
    if await is_banned(user_id):
        await callback.answer(small_caps("You are banned!"), show_alert=True)
        return
    
    await state.set_state(ThumbnailState.waiting_for_thumbnail)
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_update")]
    ])
    
    text = (
        f"<b>📸 {small_caps('Send me a photo')}</b>\n\n"
        f"<blockquote>{small_caps('This image will be used as the cover for your videos.')}</blockquote>"
    )
    
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
    
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await callback.answer()

@router.callback_query(F.data == "cancel_update")
async def cancel_update(callback: CallbackQuery, state: FSMContext, bot: Bot):
    """Cancel the thumbnail update."""
    await state.clear()
    await show_settings(callback, bot)

@router.message(ThumbnailState.waiting_for_thumbnail, F.photo)
async def receive_thumbnail(message: types.Message, state: FSMContext):
    """Save the received photo as thumbnail."""
    user_id = message.from_user.id
    file_id = message.photo[-1].file_id
    
    await set_thumbnail(user_id, file_id)
    await state.clear()
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚙️ Back to Settings", callback_data="settings")]
    ])
    
    await message.answer(
        f"<b>✅ {small_caps('Thumbnail saved!')}</b>\n\n"
        f"<blockquote>{small_caps('Your videos will now use this cover image.')}</blockquote>",
        parse_mode="HTML",
        reply_markup=keyboard
    )

@router.callback_query(F.data == "view_thumb")
async def view_thumbnail(callback: CallbackQuery, bot: Bot):
    """Show the user's current thumbnail."""
    user_id = callback.from_user.id
    thumb = await get_thumbnail(user_id)
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚙️ Back to Settings", callback_data="settings")]
    ])
    
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
    
    if thumb:
        await bot.send_photo(
            chat_id=callback.message.chat.id,
            photo=thumb,
            caption=f"<b>🖼️ {small_caps('Your Current Thumbnail')}</b>",
            parse_mode="HTML",
            reply_markup=keyboard
        )
    else:
        await bot.send_message(
            chat_id=callback.message.chat.id,
            text=f"<b>❌ {small_caps('No thumbnail set')}</b>\n\n"
                 f"<blockquote>{small_caps('Use Update Thumbnail to set one.')}</blockquote>",
            parse_mode="HTML",
            reply_markup=keyboard
        )
    await callback.answer()

@router.callback_query(F.data == "remove_thumb")
async def remove_thumbnail_handler(callback: CallbackQuery, bot: Bot):
    """Remove the user's thumbnail."""
    user_id = callback.from_user.id
    removed = await remove_thumbnail(user_id)
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚙️ Back to Settings", callback_data="settings")]
    ])
    
    if removed:
        text = (
            f"<b>🗑️ {small_caps('Thumbnail Removed')}</b>\n\n"
            f"<blockquote>{small_caps('Your videos will now be sent without a custom cover.')}</blockquote>"
        )
    else:
        text = (
            f"<b>❌ {small_caps('No thumbnail to remove')}</b>\n\n"
            f"<blockquote>{small_caps('You have not set a thumbnail yet.')}</blockquote>"
        )
    
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
    
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await callback.answer()


@router.callback_query(F.data == "close_settings")
async def close_settings(callback: CallbackQuery):
    """Close the settings menu."""
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
    await callback.answer(small_caps("Settings closed"))

