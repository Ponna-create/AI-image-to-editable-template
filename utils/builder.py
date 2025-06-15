import json
import os
from datetime import datetime

def build_template(background_path, text_layers, shapes, output_dir):
    """
    Combine all elements into a template and save as JSON.
    
    Args:
        background_path (str): Path to the cleaned background image
        text_layers (list): List of text layer information
        shapes (list): List of shape information
        output_dir (str): Directory to save the template
        
    Returns:
        dict: Template information including paths and metadata
    """
    # Create timestamp for unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create template structure
    template = {
        "metadata": {
            "created_at": timestamp,
            "version": "1.0"
        },
        "background": {
            "path": background_path,
            "type": "image"
        },
        "text_layers": text_layers,
        "shapes": shapes
    }
    
    # Save template as JSON
    template_path = os.path.join(output_dir, f"template_{timestamp}.json")
    with open(template_path, 'w') as f:
        json.dump(template, f, indent=2)
    
    return {
        "template_path": template_path,
        "template": template
    }

def export_to_canva(template, output_format="json"):
    """
    Convert template to Canva-compatible format.
    
    Args:
        template (dict): Template information
        output_format (str): Output format ("json" or "svg")
        
    Returns:
        str: Path to the exported file
    """
    # TODO: Implement Canva export format
    # This will be implemented in a future version
    pass 