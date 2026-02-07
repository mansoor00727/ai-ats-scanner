import fitz  # PyMuPDF
from docx import Document
from sentence_transformers import SentenceTransformer, util
import ollama
import os

# Load the semantic model (Local)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Change this line in nlp_engine.py
ollama_host = os.getenv('OLLAMA_HOST', 'http://host.docker.internal:11434')
client = ollama.Client(host=ollama_host)

def extract_text(file_path):
    """Extracts text based on file extension."""
    if file_path.endswith('.pdf'):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def calculate_semantic_match(resume_text, jd_text):
    """Calculates meaning-based similarity instead of just keywords."""
    resume_vec = model.encode(resume_text, convert_to_tensor=True)
    jd_vec = model.encode(jd_text, convert_to_tensor=True)
    score = util.cos_sim(resume_vec, jd_vec)
    return round(float(score[0][0]) * 100, 2)

def get_ai_advice(resume_text, jd_text):
    """Gets recruiter feedback from Local Llama 3."""
    prompt = f"Compare this Resume: {resume_text[:1000]} to this JD: {jd_text[:1000]}. Give 3 short, punchy recruiter tips."
    try:
        response = client.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception:
        return "AI Analysis unavailable. Ensure Ollama is running."

def rewrite_bullet_point(bullet_point):
    """Rewrites a single point for maximum impact."""
    prompt = f"Rewrite this resume bullet point to be more impactful for a Canadian tech role: {bullet_point}"
    try:
        response = client.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception:
        return "Rewrite failed. Check Ollama connection."