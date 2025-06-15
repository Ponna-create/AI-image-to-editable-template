# AI Image to Editable Template Converter

Convert AI-generated images into editable design templates with separated layers (text, shapes, background).

## Features

- Upload AI-generated images
- Extract text using OCR
- Remove text from background
- Detect and vectorize shapes
- Export as editable template

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
- Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
- Linux: `sudo apt-get install tesseract-ocr`

3. Run the application:
```bash
python app.py
```

4. Visit `http://localhost:5000`

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the service:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variables**:
     - `FLASK_ENV`: production
     - `SECRET_KEY`: your-secret-key

## Project Structure

```
project/
├── app.py              # Flask application
├── templates/          # HTML templates
├── static/            # Static files
│   ├── uploads/       # Uploaded images
│   └── outputs/       # Processed images
├── utils/             # Utility modules
│   ├── ocr.py         # Text extraction
│   ├── inpaint.py     # Background cleanup
│   ├── vectorize.py   # Shape detection
│   └── builder.py     # Template building
└── requirements.txt   # Dependencies
```

## Environment Variables

- `FLASK_ENV`: Set to 'production' in production
- `SECRET_KEY`: Flask secret key
- `PORT`: Port number (default: 5000)

## License

MIT 