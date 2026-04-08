import React, { useState } from 'react';
import axios from 'axios';
import DocumentUpload from './components/DocumentUpload';
import ResultsDisplay from './components/ResultsDisplay';
import LoadingIndicator from './components/LoadingIndicator';
import './App.css';

function App() {
    const [results, setResults] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleUpload = async (file) => {
        const formData = new FormData();
        formData.append('file', file);

        setIsLoading(true);
        setError(null);
        setResults(null);

        try {
            const response = await axios.post('/api/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setResults(response.data);
        } catch (err) {
            setError('An error occurred during processing. Please try again.');
            console.error(err);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Document Processing Service</h1>
            </header>
            <main>
                {!isLoading && <DocumentUpload onUpload={handleUpload} isLoading={isLoading} />}
                {isLoading && <LoadingIndicator />}
                {error && <div className="error-message">{error}</div>}
                {!isLoading && <ResultsDisplay data={results} />}
            </main>
        </div>
    );
}

export default App;
