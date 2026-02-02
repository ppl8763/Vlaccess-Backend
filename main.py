from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.video import router as video_router

app = FastAPI(title="DeepStream Video Processing API")

# === CORS Middleware ===
origins = [
    "http://localhost:5173",  # React dev server (Vite default)
    "http://localhost:3000",  # If using CRA
    # Add your production URLs here, e.g. "https://yourdomain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow these origins
    allow_credentials=True,      # allow cookies
    allow_methods=["*"],         # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],         # allow all headers
)

# Include your routes
app.include_router(video_router)

@app.get("/")
def health_check():
    return {"status": "OK"}
