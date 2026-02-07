# Use Python 3.12 slim image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Copy additional requirements from subdirectory
COPY ai_ats_scanner/requirements.txt ./ai_ats_scanner_requirements.txt

# Install Python dependencies
# First install the main reflex version, then install other dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir \
    pymupdf==1.23.25 \
    spacy==3.7.4 \
    scikit-learn==1.4.1.post1 \
    sentence-transformers==2.5.1 \
    ollama==0.1.7 \
    python-dotenv==1.0.1 \
    google-genai==0.3.0 \
    pandas==2.2.1 \
    python-docx

# Download spaCy model (using pip for reliable installation)
RUN pip install --no-cache-dir https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl

# Copy the application code
COPY . .

# Initialize Reflex
RUN reflex init

# Expose Reflex ports
# 3000 - Frontend
# 8000 - Backend API
EXPOSE 3000 8000

# Run the application
CMD ["reflex", "run", "--env", "prod", "--loglevel", "info"]
