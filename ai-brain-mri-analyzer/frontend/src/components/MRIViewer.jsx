import React, { useState } from 'react';
import axios from 'axios';

const MRIViewer = () => {
    const [image, setImage] = useState(null);
    const [analysisResult, setAnalysisResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setImage(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const analyzeImage = async () => {
        if (!image) return;

        setLoading(true);
        try {
            const response = await axios.post('/api/analyze', { image });
            setAnalysisResult(response.data);
        } catch (error) {
            console.error('Error analyzing image:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>MRI Viewer</h1>
            <input type="file" accept="image/*" onChange={handleImageUpload} />
            <button onClick={analyzeImage} disabled={loading}>
                {loading ? 'Analyzing...' : 'Analyze MRI'}
            </button>
            {image && <img src={image} alt="Uploaded MRI" style={{ width: '100%', maxHeight: '400px' }} />}
            {analysisResult && (
                <div>
                    <h2>Analysis Result:</h2>
                    <pre>{JSON.stringify(analysisResult, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default MRIViewer;