# Document Analyzer AI

This project is a web-based application designed to analyze uploaded documents (PDFs and images) using Artificial Intelligence. It extracts key information, classifies the document type, and determines its validity based on the content.

## Live Demo

The application is deployed on Vercel and can be accessed here:

**[https://document-analyzer-theta.vercel.app/](https://document-analyzer-theta.vercel.app/)**

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
-   **Deployment:** Configured for easy deployment to **Vercel**

## How to Run

For detailed instructions on how to set up the local development environment and deploy the application to Vercel, please refer to the Quickstart Guide located at `/quickstart.md`.

