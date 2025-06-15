import cv2
import numpy as np

def remove_text(image_path, text_boxes, output_path):
    """
    Remove text from an image using inpainting.
    
    Args:
        image_path (str): Path to the input image
        text_boxes (list): List of dictionaries containing text box information
        output_path (str): Path to save the cleaned image
        
    Returns:
        str: Path to the cleaned image
    """
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image at {image_path}")
    
    # Create mask
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    
    # Add text boxes to mask
    for box in text_boxes:
        x, y = box['x'], box['y']
        w, h = box['width'], box['height']
        # Add padding to ensure complete text removal
        padding = 2
        cv2.rectangle(mask, 
                     (x - padding, y - padding),
                     (x + w + padding, y + h + padding),
                     255, -1)
    
    # Perform inpainting
    cleaned_image = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    
    # Save result
    cv2.imwrite(output_path, cleaned_image)
    
    return output_path 