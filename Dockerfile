# # Use Ubuntu base image
# FROM ubuntu:20.04

# # Set your GitHub username and token as build arguments
# # ARG GITHUB_USERNAME
# # ARG GITHUB_TOKEN

# # Set ENV variables that can be used in the container
# # ENV GITHUB_USERNAME=${GITHUB_USERNAME}
# # ENV GITHUB_TOKEN=${GITHUB_TOKEN}

# # Update the package manager and install any packages you need
# RUN apt update && \
#     apt install python3 -y && \
#     apt-get install -y git && \
#     cd /opt && \
#     #clone the repo source code
#     # git clone -b nishant https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/barualee/NexoSphere.git && \
#     #run installs
#     apt install pip -y

# WORKDIR /app
# COPY ./nexosphere .
# # Copy requirements.txt first (this helps with caching layers)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 9874
# EXPOSE 443

# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=nexosphere
ENV FLASK_ENV=production

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY nexosphere nexosphere

# Change to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 5000
# EXPOSE 9874

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]