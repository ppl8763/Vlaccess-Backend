import os
import subprocess
from datetime import datetime
from bson import ObjectId
from core.config import CHUNK_DURATION_SEC
from models.video_chunk import VideoChunk
from core.database import video_chunks_collection

async def split_and_store_chunks(video_id, video_path, duration):
    os.makedirs("/data/chunks", exist_ok=True)

    chunks_array = []
    index = 0

    for start in range(0, duration, CHUNK_DURATION_SEC):
        end = min(start + CHUNK_DURATION_SEC, duration)
        output_path = f"/data/chunks/{video_id}_{index}.mp4"

        cmd = [
            "ffmpeg",
            "-ss", str(start),
            "-i", video_path,
            "-t", str(end - start),
            "-c", "copy",
            output_path
        ]

        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        chunk = VideoChunk(
            video_id=ObjectId(str(video_id)) if not isinstance(video_id, ObjectId) else video_id,
            chunk_index=index,
            start_sec=start,
            end_sec=end,
            chunk_path=output_path
        )


        chunk_dict = {
            "_id": ObjectId(),
            "chunk_index": chunk.chunk_index,
            "start_sec": chunk.start_sec,
            "end_sec": chunk.end_sec,
            "chunk_path": chunk.chunk_path,
            "status": chunk.status,
            "created_at": chunk.created_at
        }

        chunks_array.append(chunk_dict)
        index += 1


    if chunks_array:
        chunks_document = {
            "_id": video_id,
            "video_id": video_id,
            "chunks": chunks_array,
            "total_chunks": len(chunks_array),
            "status":chunk.status,
            "created_at": datetime.utcnow()
        }
        await video_chunks_collection.insert_one(chunks_document)
