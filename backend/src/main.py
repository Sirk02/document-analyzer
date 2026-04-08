from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import documents
import os

app = FastAPI()

# Configure CORS for local development and Vercel deployments
origins = [
    "http://localhost:3000",
]

# Add the Vercel preview URL to the allowed origins if it exists
vercel_url = os.environ.get("VERCEL_URL")
if vercel_url:
    origins.append(f"https://{vercel_url}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Processing API"}
