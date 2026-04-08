# Document Analyzer AI

This project is a web-based application designed to analyze uploaded documents (PDFs and images) using Artificial Intelligence. It extracts key information, classifies the document type, and determines its validity based on the content.

This is a local-only application and is not intended for public deployment.

## Features

-   **File Upload:** Supports PDF and common image formats.
-   **AI-Powered Analysis:** Utilizes the OpenAI Vision API (`gpt-4o-mini`) to "read" the document and extract structured data.
-   **Data Extraction:** Identifies and extracts key fields such as:
    -   Name (person or company)
    -   Identification Number
    -   Monetary Amount
    -   Currency
-   **Document Classification:** Categorizes documents as "Invoice," "Contract," "Personal ID," etc.
-   **Validity Check:** Provides a simple "valid" or "invalid" status with a brief explanation.

## Tech Stack

-   **Backend:** Python with **FastAPI**
-   **Frontend:** JavaScript with **React**
-   **AI Model:** OpenAI **GPT-4o-mini**

## How to Run

For detailed instructions on how to set up and run the local development environment, please refer to the `quickstart.md` file located in the `/specs/001-document-processing-service/` directory.
