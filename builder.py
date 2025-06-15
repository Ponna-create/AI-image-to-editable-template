# builder.py

def build_editable_template(image_path, ocr_data, output_path):
    with open(output_path, 'w') as f:
        f.write("<html><body>")
        for item in ocr_data:
            f.write(f"<div>{item['text']}</div>")
        f.write("</body></html>")
