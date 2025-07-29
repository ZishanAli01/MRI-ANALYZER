import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const fetchMRIAnalysis = async (imageData) => {
    try {
        const response = await axios.post(`${API_URL}/analyze`, imageData);
        return response.data;
    } catch (error) {
        console.error('Error fetching MRI analysis:', error);
        throw error;
    }
};