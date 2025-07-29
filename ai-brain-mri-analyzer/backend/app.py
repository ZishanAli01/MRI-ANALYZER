from flask import Flask, request, jsonify
from models.pytorch_model import BrainMRIModel
from utils.image_processing import load_image, preprocess_image
from algorithms.graph_traversal import bfs
from algorithms.linked_list import LinkedList

app = Flask(__name__)
model = BrainMRIModel()

@app.route('/api/analyze', methods=['POST'])
def analyze_mri():
    data = request.json
    image_path = data.get('image_path')
    
    if not image_path:
        return jsonify({'error': 'No image path provided'}), 400
    
    image = load_image(image_path)
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    
    # Example of using graph traversal on the prediction
    graph_representation = create_graph_from_prediction(prediction)
    traversal_result = bfs(graph_representation)
    
    return jsonify({'prediction': prediction, 'traversal_result': traversal_result})

def create_graph_from_prediction(prediction):
    # Placeholder function to create a graph representation from the prediction
    return {}

if __name__ == '__main__':
    app.run(debug=True)