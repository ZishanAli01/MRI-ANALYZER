# AI-Based Brain MRI Analyzer - Frontend Documentation

## Overview
The AI-Based Brain MRI Analyzer is a web application designed to analyze brain MRI images using advanced machine learning techniques. The frontend is built with React, providing a user-friendly interface for uploading MRI images and viewing analysis results.

## Project Structure
The frontend of the application is organized as follows:

```
frontend
├── src
│   ├── App.jsx                # Main application component
│   ├── components
│   │   └── MRIViewer.jsx      # Component for displaying MRI images and results
│   ├── pages
│   │   └── Home.jsx           # Landing page component
│   └── utils
│       └── api.js             # API utility functions for backend communication
├── package.json                # NPM configuration file
└── README.md                   # Documentation for the frontend
```

## Getting Started

### Prerequisites
- Node.js and npm installed on your machine.

### Installation
1. Navigate to the frontend directory:
   ```
   cd frontend
   ```
2. Install the dependencies:
   ```
   npm install
   ```

### Running the Application
To start the development server, run:
```
npm start
```
This will launch the application in your default web browser at `http://localhost:3000`.

## Features
- Upload MRI images for analysis.
- View processed images and analysis results.
- User-friendly interface with navigation to different sections of the application.

## API Integration
The frontend communicates with the Flask backend through API calls defined in `src/utils/api.js`. Key functions include:
- `fetchMRIAnalysis`: Retrieves analysis results from the server.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.