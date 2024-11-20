# Use official Python image as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the application source code
COPY src/ /app/

# Expose the port the app will run on
EXPOSE 4743

# Start the app
CMD ["python", "app.py"]
