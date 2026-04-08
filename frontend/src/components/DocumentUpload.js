import React, { useState } from 'react';

const DocumentUpload = ({ onUpload, isLoading }) => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        if (event.target.files && event.target.files[0]) {
            setSelectedFile(event.target.files[0]);
        }
    };

    const handleUpload = () => {
        if (selectedFile) {
            onUpload(selectedFile);
        }
    };

    return (
        <div className="upload-container">
            <h2>Upload a Document</h2>
            <div className="file-input-wrapper">
                <input 
                    type="file" 
                    aria-label="Upload Document" 
                    onChange={handleFileChange} 
                    accept="image/*,application/pdf" 
                />
                <div className="file-input-label">
                    {selectedFile ? `Selected: ${selectedFile.name}` : "Click to select a file or drag and drop"}
                </div>
            </div>
            <button onClick={handleUpload} disabled={!selectedFile || isLoading}>
                {isLoading ? 'Processing...' : 'Upload and Process'}
            </button>
        </div>
    );
};

export default DocumentUpload;
