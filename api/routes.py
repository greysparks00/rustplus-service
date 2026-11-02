from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import APIRouter

router = APIRouter()

TIME_ZONE = ZoneInfo("America/Chicago")

@router.get("/now")
async def now():
    current_time = datetime.now(TIME_ZONE)

    return {
        "datetime": current_time.isoformat(),
        "timezone": TIME_ZONE
    }