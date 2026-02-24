from plugins.start import router as start_router
from plugins.settings import router as settings_router
from plugins.video import router as video_router
from plugins.admin import router as admin_router

__all__ = ["start_router", "settings_router", "video_router", "admin_router"]
