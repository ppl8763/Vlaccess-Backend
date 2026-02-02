from datetime import datetime

class VideoChunk:
    def __init__(
        self,
        video_id,
        chunk_index: int,
        start_sec: int,
        end_sec: int,
        chunk_path: str,
    ):
        self.video_id = video_id
        self.chunk_index = chunk_index
        self.start_sec = start_sec
        self.end_sec = end_sec
        self.chunk_path = chunk_path
        self.status = "PENDING"
        self.created_at = datetime.utcnow()
