# Quickstart: Document Processing Service

This guide provides instructions on how to set up and run the project locally.

## Prerequisites

- Python 3.9+ and Pip
- Node.js 20+ and Npm
- Poppler (for PDF processing).
  - **macOS**: `brew install poppler`
  - **Ubuntu**: `sudo apt-get install poppler-utils`
  - **Fedora**: `sudo dnf install poppler-utils`
  - **Windows**: Download from the Poppler for Windows page.

## Backend Setup (FastAPI)

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

3.  **Create and configure your environment variables:**
    Create a file named `.env` inside the `backend` directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY='your-api-key-here'
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the backend server:**
    ```bash
    uvicorn src.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.
## Frontend Setup (React)

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install JavaScript dependencies:**
    ```bash
    npm install
    ```

3.  **Run the frontend development server:**
    ```bash
    npm start
    ```
    The React application will open automatically in your browser at `http://localhost:3000`.

## Running the Application

Ensure both the backend and frontend servers are running in separate terminal windows. You can then access the application by navigating to `http://localhost:3000` in your web browser.

