# 🤖 AI-Powered ATS Resume Scanner

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Reflex](https://img.shields.io/badge/reflex-0.4.8-purple.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

An intelligent **Applicant Tracking System (ATS)** powered by local LLMs that analyzes resumes against job descriptions, providing semantic matching scores and AI-driven recruitment advice.

## ✨ Features

- **📊 Batch Resume Analysis**: Upload multiple resumes (PDF/DOCX) simultaneously
- **🎯 Semantic Matching**: Advanced NLP-based scoring using sentence transformers
- **🤖 AI Recruiter Insights**: Get strategic hiring advice powered by local Ollama LLMs
- **📈 Skill Visualization**: Interactive radar charts showing candidate competencies
- **✍️ Resume Point Improver**: AI-powered bullet point optimization for Canadian job market
- **🔒 Privacy First**: All processing happens locally - no data leaves your machine

## 🏗️ Architecture

```
ai-ats-scanner/
├── ai_ats_scanner/
│   ├── ai_ats_scanner.py    # Main Reflex application
│   ├── nlp_engine.py        # NLP and LLM integration
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Container configuration
├── assets/                  # Static assets
├── docker-compose.yml       # Multi-container orchestration
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- [Ollama](https://ollama.ai) installed locally
- Docker & Docker Compose (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mansoor00727/ai-ats-scanner.git
   cd ai-ats-scanner
   ```

2. **Install dependencies**
   ```bash
   pip install -r ai_ats_scanner/requirements.txt
   ```

3. **Download required models**
   ```bash
   # Download spaCy model
   python -m spacy download en_core_web_sm
   
   # Pull Ollama model
   ollama pull llama2
   ```

4. **Run the application**
   ```bash
   cd ai_ats_scanner
   reflex run
   ```

5. **Open your browser** to `http://localhost:3000`

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

## 📖 Usage

1. **Paste Job Description**: Copy-paste the full job description into the text area
2. **Upload Resumes**: Select one or multiple resume files (PDF/DOCX)
3. **Analyze**: Click "Analyze Batch" to process all resumes
4. **Review Results**:
   - View ranked candidates by match percentage
   - Read AI-generated strategic advice for top candidate
   - Explore skill radar chart visualization
5. **Improve Resume Points**: Use the built-in optimizer to enhance bullet points

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|--------|
| **Reflex** | Full-stack Python web framework |
| **Ollama** | Local LLM inference (Llama 2) |
| **spaCy** | Natural language processing |
| **Sentence Transformers** | Semantic similarity matching |
| **scikit-learn** | ML utilities and metrics |
| **PyMuPDF** | PDF text extraction |
| **python-docx** | DOCX document parsing |

## 🧠 How It Works

```python
# Semantic matching pipeline
resume_text = extract_text(resume_file)
score = calculate_semantic_match(resume_text, job_description)
advice = get_ai_advice(resume_text, job_description)  # Powered by Llama 2
```

### Scoring Algorithm

1. **Text Extraction**: Parse PDF/DOCX using PyMuPDF and python-docx
2. **Embedding Generation**: Convert texts to vectors using `sentence-transformers`
3. **Cosine Similarity**: Calculate semantic match (0-100%)
4. **AI Analysis**: Generate contextual hiring insights via Ollama

## 🎯 Example Output

```
┌─────────────────────────────────────────────┐
│ Candidate Leaderboard                       │
├─────────────────────────────────────────────┤
│ john_doe.pdf              ██████████ 87%    │
│ jane_smith.pdf            ████████░░ 82%    │
│ alex_wong.pdf             ███████░░░ 76%    │
└─────────────────────────────────────────────┘

🚩 AI Recruiter's Strategic Advice:
John shows strong backend expertise with 5+ years in Python/Django.
Consider technical interview focusing on distributed systems...
```

## ⚙️ Configuration

Create a `.env` file (optional):

```bash
OLLAMA_MODEL=llama2
EMBEDDING_MODEL=all-MiniLM-L6-v2
MAX_UPLOAD_SIZE=10MB
```

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📝 License

MIT License - see LICENSE file for details

## 🔮 Roadmap

- [ ] Support for LinkedIn profile parsing
- [ ] Multi-language resume support
- [ ] Custom skill taxonomy configuration
- [ ] Export reports as PDF
- [ ] Integration with HR platforms (Greenhouse, Lever)

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using local AI - Your data never leaves your machine**


# 🚀 AI-Powered ATS Resume Suite (Local & Private)

A production-grade, full-stack ATS (Applicant Tracking System) suite designed to bridge the gap between candidates and recruiters. This tool leverages **Local LLMs** and **Semantic Search** to rank resumes and provide actionable career coaching without compromising data privacy.


> **Insert Screenshot 1: The main dashboard with a Job Description and uploaded resumes here.**

---

## 🌟 Key Features

- **Batch Resume Processing:** Upload multiple PDFs or Word docs simultaneously.
- **Semantic Ranking:** Uses `all-MiniLM-L6-v2` transformers to understand skill context beyond simple keywords.
- **Privacy-First AI:** Integrated with **Ollama (Llama 3)** to run all AI analysis locally on your hardware.
- **Skill Gap Visualization:** Interactive **Radar Charts** to visualize how well a candidate fits a role.
- **Resume Point Improver:** An AI-driven "Optimizer" that transforms weak bullet points into high-impact, results-oriented achievements.
- **Clipboard Integration:** One-click copy for optimized resume points.

---

## 🛠️ Technical Architecture



- **Frontend/Backend:** [Reflex](https://reflex.dev/) (Pure Python Full-stack Framework)
- **AI Engine:** [Ollama](https://ollama.com/) (Llama 3)
- **NLP & Embeddings:** Sentence-Transformers, PyMuPDF, Python-Docx
- **Containerization:** Docker (Multi-stage build)
- **Environment:** Windsor, Ontario, Canada 🇨🇦

---

## 🚀 Getting Started

### Prerequisites
- Docker Desktop
- Ollama (Running locally)

### Installation & Deployment

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-ats-scanner.git](https://github.com/YOUR_USERNAME/ai-ats-scanner.git)
   cd ai-ats-scanner