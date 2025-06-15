import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image(output_path='static/uploads/test_image.png'):
    # Create directories if they don't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create a white background
    width, height = 800, 600
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Add some shapes
    # Rectangle
    draw.rectangle([(100, 100), (300, 200)], fill='#FFB6C1', outline='black')
    
    # Circle
    draw.ellipse([(400, 100), (600, 300)], fill='#87CEEB', outline='black')
    
    # Triangle
    draw.polygon([(200, 400), (300, 300), (400, 400)], fill='#98FB98', outline='black')
    
    # Add text
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Add different text elements
    texts = [
        ("Welcome to", (100, 250), (0, 0, 0)),
        ("AI Template", (100, 300), (255, 0, 0)),
        ("Converter", (100, 350), (0, 0, 255))
    ]
    
    for text, pos, color in texts:
        draw.text(pos, text, fill=color, font=font)
    
    # Save the image
    image.save(output_path)
    print(f"Test image created at: {output_path}")
    return output_path

if __name__ == "__main__":
    create_test_image() 