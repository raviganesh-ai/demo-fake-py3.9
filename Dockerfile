# Use official Python 3.12 image to run this demo application and tests
FROM python:3.12-slim

# Ensure Python outputs are not buffered and UTF-8 is used by default
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Default command runs tests; adjust as needed for your use case
CMD ["pytest", "-q"]
