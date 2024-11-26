# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY nexosphere nexosphere

# Copy the application code
COPY .env nexosphere

# Expose the port the app runs on
EXPOSE 5001
EXPOSE 8501

# Run the application
CMD ["python3", "./nexosphere/main.py"]