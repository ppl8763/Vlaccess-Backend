from pydantic import BaseModel
from typing import Optional

class VideoCreate(BaseModel):
    video_path: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None  # USER_GPS | MANUAL | SYSTEM
    time_of_day: str    # MORNING | AFTERNOON | EVENING | NIGHT
