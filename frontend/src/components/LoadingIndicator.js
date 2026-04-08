import React, { useState, useEffect } from 'react';
import './LoadingIndicator.css';

const LoadingIndicator = () => {
    const [currentStep, setCurrentStep] = useState(0);
    const steps = [
        "Uploading document...",
        "Analyzing content...",
        "Extracting key information...",
        "Finalizing results..."
    ];

    useEffect(() => {
        const timer = setInterval(() => {
            setCurrentStep(prevStep => {
                if (prevStep < steps.length - 1) {
                    return prevStep + 1;
                }
                return prevStep;
            });
        }, 3000);

        return () => clearInterval(timer);
    }, [steps.length]);

    return (
        <div className="loading-container">
            <h3>Processing...</h3>
            <div className="loading-steps">
                <div className="step active">
                    {steps[currentStep]}
                </div>
            </div>
        </div>
    );
};

export default LoadingIndicator;
