# AI-Based Brain MRI Analyzer

This project is an AI-based application designed to analyze brain MRI images using machine learning techniques. The application is structured into two main components: a Flask backend and a React frontend.

## Project Structure

```
ai-brain-mri-analyzer
├── backend
│   ├── app.py                # Entry point for the Flask backend application
│   ├── requirements.txt      # Lists dependencies for the backend
│   ├── models
│   │   └── pytorch_model.py  # Contains the PyTorch model for MRI analysis
│   ├── algorithms
│   │   ├── linked_list.py    # Implements linked list data structure
│   │   └── graph_traversal.py # Implements graph traversal algorithms
│   └── utils
│       └── image_processing.py # Utility functions for image processing
├── frontend
│   ├── src
│   │   ├── App.jsx           # Main component of the React application
│   │   ├── components
│   │   │   └── MRIViewer.jsx  # Component for displaying MRI images
│   │   ├── pages
│   │   │   └── Home.jsx      # Landing page of the application
│   │   └── utils
│   │       └── api.js        # Functions for making API calls to the backend
│   ├── package.json          # Configuration file for npm
│   └── README.md             # Documentation for the frontend part of the project
└── README.md                 # Overall documentation for the entire project
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies using npm:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

- Access the frontend application in your web browser at `http://localhost:3000`.
- Upload brain MRI images for analysis and view the results.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.