import cv2
import numpy as np
from PIL import Image
import json

def detect_shapes(image_path):
    """
    Detect basic shapes in an image and convert them to vector format.
    
    Args:
        image_path (str): Path to the input image
        
    Returns:
        list: List of dictionaries containing shape information
    """
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image at {image_path}")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    shapes = []
    for contour in contours:
        # Get shape properties
        area = cv2.contourArea(contour)
        if area < 100:  # Filter out noise
            continue
            
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)
        
        # Approximate the shape
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Determine shape type
        shape_type = "unknown"
        if len(approx) == 3:
            shape_type = "triangle"
        elif len(approx) == 4:
            # Check if it's a rectangle or square
            aspect_ratio = float(w)/h
            if 0.95 <= aspect_ratio <= 1.05:
                shape_type = "square"
            else:
                shape_type = "rectangle"
        elif len(approx) > 4:
            # Check if it's a circle
            circularity = 4 * np.pi * area / (cv2.arcLength(contour, True) ** 2)
            if circularity > 0.8:
                shape_type = "circle"
            else:
                shape_type = "polygon"
        
        # Get color
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [contour], -1, 255, -1)
        mean_color = cv2.mean(image, mask=mask)[:3]
        
        shapes.append({
            'type': shape_type,
            'x': int(x),
            'y': int(y),
            'width': int(w),
            'height': int(h),
            'color': [int(c) for c in mean_color],
            'points': contour.reshape(-1, 2).tolist()
        })
    
    return shapes 