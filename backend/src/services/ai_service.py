import base64
import json
from openai import OpenAI
from decouple import config
from pdf2image import convert_from_bytes
import io

# Load the API key from the .env file
api_key = config('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file.")

client = OpenAI(api_key=api_key)

def get_image_base64(file_bytes: bytes, content_type: str) -> list[str]:
    """Converts image or PDF bytes into a list of base64-encoded images."""
    base64_images = []
    if content_type.startswith('image/'):
        base64_images.append(base64.b64encode(file_bytes).decode('utf-8'))
    elif content_type == 'application/pdf':
        images = convert_from_bytes(file_bytes)
        for image in images:
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            base64_images.append(base64.b64encode(buffered.getvalue()).decode('utf-8'))
    return base64_images

def analyze_document_with_ai(base64_images: list[str]):
    """
    Sends images to the OpenAI Vision API and asks it to extract structured data.
    """
    if not base64_images:
        return {"error": "No images to process."}

    prompt_messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
                    Analyze the following document image and extract the following information in a structured JSON format.
                    The required fields are:
                    - "name": The full name of the primary person or company.
                    - "id_number": The primary identification number (like a DPI, passport number, etc.), returned as a string.
                    - "amount": The main monetary value or total amount. IMPORTANT: This must be a numeric type (float or integer), not a string. Do not include currency symbols or commas.
                    - "currency": The currency of the amount (e.g., "Q", "USD", "€"). This should be a string.
                    - "category": Classify the document into one of the following: "Invoice", "Contract", "Legal Document", "Personal ID", "Other".
                    
                    Based on the extracted data, also determine if the document is valid using these strict rules:
                    - "is_valid": A boolean (true or false). A document is ONLY considered 'true' if it is clear, undamaged, and confidently classified into a primary category ("Invoice", "Contract", "Legal Document", "Personal ID"). If the document is blurry, damaged, a simple receipt, or classified as "Other", this MUST be 'false'.
                    - "validation_reason": A brief explanation for the validity status. If invalid, explain why (e.g., "Document is blurry and unreadable", "Unrecognized document type", "Document appears to be a simple receipt, not a formal invoice.").
                    
                    If a field is not present, return null for its value.
                    Your response MUST be only the JSON object, with no additional text or explanations. Your response should be as fast as possible.
                    """
                },
                *map(lambda img: {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img}"}}, base64_images)
            ]
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=prompt_messages,
            max_tokens=256,
        )
        
        response_text = response.choices[0].message.content
        json_response_string = response_text.strip().replace("```json", "").replace("```", "").strip()
        
        return json.loads(json_response_string)

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return {"error": "Failed to communicate with OpenAI API."}

async def process_document(file_bytes: bytes, content_type: str):
    """Main function to process a document."""
    base64_images = get_image_base64(file_bytes, content_type)
    if not base64_images:
        return {"error": "Could not convert file to images."}
        
    analysis_result = analyze_document_with_ai(base64_images)
    return analysis_result
