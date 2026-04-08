from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import documents

app = FastAPI()

# Configure CORS for local development
origins = [
    "http://localhost:3000",
]

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
