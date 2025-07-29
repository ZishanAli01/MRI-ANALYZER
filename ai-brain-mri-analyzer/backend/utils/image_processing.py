def load_image(image_path):
    from PIL import Image
    import numpy as np

    # Load an image from the specified path
    image = Image.open(image_path)
    return np.array(image)

def preprocess_image(image_array):
    import cv2

    # Convert to grayscale
    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    # Resize image to a fixed size (e.g., 256x256)
    resized_image = cv2.resize(gray_image, (256, 256))
    # Normalize pixel values to [0, 1]
    normalized_image = resized_image / 255.0
    return normalized_image

def augment_image(image_array):
    from torchvision import transforms

    # Define a series of augmentations
    augmentation_pipeline = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    ])

    # Convert to PIL Image for augmentation
    pil_image = Image.fromarray((image_array * 255).astype('uint8'))
    augmented_image = augmentation_pipeline(pil_image)
    return np.array(augmented_image)