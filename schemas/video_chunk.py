from pydantic import BaseModel

class VideoChunkResponse(BaseModel):
    chunk_index: int
    start_sec: int
    end_sec: int
    status: str
