from fastapi import APIRouter, HTTPException
from schemas.video import VideoCreate
from core.database import videos_collection,video_chunks_collection
from models.video import Video
from utils.video_utils import get_video_duration
from utils.chunker import split_and_store_chunks
from bson import ObjectId
from utils import mongo_serializer

router = APIRouter(prefix="/videos", tags=["Videos"])

@router.post("/")
async def create_video(video: VideoCreate):
    try:
        duration = get_video_duration(video.video_path)

        video_doc = Video(
            video_path=video.video_path,
            duration_sec=duration,
            time_of_day=video.time_of_day,
            latitude=video.latitude,
            longitude=video.longitude,
            
        )

        result = await videos_collection.insert_one(video_doc.__dict__)
        video_id = result.inserted_id

        await split_and_store_chunks(video_id, video.video_path, duration)

        await videos_collection.update_one(
            {"_id": video_id},
            {"$set": {"status": "SPLIT"}}
        )

        return {
            "video_id": str(video_id),
            "duration_sec": duration,
            "status": "SPLIT"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/get")
async def get_all_videos():
    videos = []

    cursor = video_chunks_collection.find({"status": "PENDING"})  # find ALL
    
    async for video in cursor:
        video["_id"] = str(video["_id"])

        
        if "video_id" in video:
            video["video_id"] = str(video["video_id"])

        if "chunks" in video:
            for chunk in video["chunks"]:
                if "_id" in chunk:
                    chunk["_id"] = str(chunk["_id"])

        videos.append(video)

    if not videos:
        raise HTTPException(status_code=404, detail="No videos found")

    return videos