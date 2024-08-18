# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements
COPY src/ /app/
COPY requirements.txt /app/

# Version 1: Copy the sales data into the image
#COPY data/ /app/data/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point for the container
ENTRYPOINT ["python", "app.py"]
