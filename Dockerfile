# Use a lightweight Python 3.10 image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Render (Render expects your app to listen on port 5000)
EXPOSE 5000

# Start the Flask app using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
