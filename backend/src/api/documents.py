from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services import ai_service
import uuid

router = APIRouter()

@router.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/') and file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Unsupported file type. Please upload an image or a PDF.")
    
    try:
        file_bytes = await file.read()
        
        # Call the new AI service to process the document
        result = await ai_service.process_document(file_bytes, file.content_type)
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        # Add metadata and return the result from the AI
        return {
            "data_id": str(uuid.uuid4()),
            "document_id": str(uuid.uuid4()),
            **result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
