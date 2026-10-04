# Use official Python 3.12 slim image to run this simple utility project
FROM python:3.12-slim

# Ensure pip is up to date for Python 3.12
RUN python -m pip install --upgrade pip

# Create and set working directory
WORKDIR /app

# Copy requirement specification and install dependencies first for better layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Default command runs the test suite; override as needed
CMD ["pytest", "-q"]
