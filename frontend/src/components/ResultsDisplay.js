import React from 'react';

const ResultsDisplay = ({ data }) => {
    if (!data) {
        return null;
    }

    const { name, id_number, amount, currency, category, is_valid, validation_reason } = data;
    const numericAmount = parseFloat(amount);

    return (
        <div className="results-container">
            <h2>Processing Results</h2>
            <div className={`status ${is_valid ? 'valid' : 'invalid'}`}>
                <strong>Status:</strong> {is_valid ? 'Valid' : 'Invalid'}
                <p>{validation_reason}</p>
            </div>
            <div className="details">
                <p><strong>Category:</strong> {category}</p>
                <p><strong>Name:</strong> {name || 'N/A'}</p>
                <p><strong>ID Number:</strong> {id_number || 'N/A'}</p>
                <p><strong>Amount:</strong> {!isNaN(numericAmount) ? `${currency || '$'}${numericAmount.toFixed(2)}` : 'N/A'}</p>
            </div>
        </div>
    );
};

export default ResultsDisplay;
