import pytesseract
import cv2
import numpy as np

def extract_text(image_path):
    """
    Extract text and bounding boxes from an image using Tesseract OCR.
    
    Args:
        image_path (str): Path to the input image
        
    Returns:
        list: List of dictionaries containing text and bounding box information
    """
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image at {image_path}")
    
    # Convert to RGB (Tesseract expects RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Get OCR data
    ocr_data = pytesseract.image_to_data(image_rgb, output_type=pytesseract.Output.DICT)
    
    # Process results
    text_boxes = []
    n_boxes = len(ocr_data['text'])
    
    for i in range(n_boxes):
        if int(ocr_data['conf'][i]) > 60:  # Filter by confidence
            text = ocr_data['text'][i]
            if text.strip():  # Only include non-empty text
                text_boxes.append({
                    'text': text,
                    'x': ocr_data['left'][i],
                    'y': ocr_data['top'][i],
                    'width': ocr_data['width'][i],
                    'height': ocr_data['height'][i],
                    'confidence': ocr_data['conf'][i]
                })
    
    return text_boxes 