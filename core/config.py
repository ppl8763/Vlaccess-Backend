import os

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://pinkun:pinkun@cluster0.eytm51q.mongodb.net/"
)

DB_NAME = "deepstream_video_db1"
CHUNK_DURATION_SEC = 15 * 60
