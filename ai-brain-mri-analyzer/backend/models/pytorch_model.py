class BrainMRIModel:
    def __init__(self, model_path):
        import torch
        self.model = torch.load(model_path)
        self.model.eval()

    def predict(self, image_tensor):
        with torch.no_grad():
            output = self.model(image_tensor)
        return output

    @classmethod
    def load_model(cls, model_path):
        return cls(model_path)