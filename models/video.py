from datetime import datetime
from typing import Optional

class Video:
    def __init__(
        self,
        video_path: str,
        duration_sec: int,
        time_of_day: str,
        latitude: Optional[float],
        longitude: Optional[float],
    ):
        self.video_path = video_path
        self.duration_sec = duration_sec
        self.time_of_day = time_of_day
        self.latitude = latitude
        self.longitude = longitude
        self.status = "PENDING"
        self.created_at = datetime.utcnow()
