FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 1. Copy the main requirements file
COPY requirements.txt .

# 2. FORCE install python-docx and other core dependencies 
# directly to the container's system python
RUN pip install --no-cache-dir reflex pymupdf spacy scikit-learn sentence-transformers ollama python-docx

# 3. Download the spaCy model explicitly
RUN python -m spacy download en_core_web_sm

# 4. Copy the rest of the project
COPY . .

# 5. Initialize reflex
RUN reflex init

EXPOSE 3000 8000

CMD ["reflex", "run", "--env", "prod"]