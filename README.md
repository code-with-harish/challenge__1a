# Challenge 1A – Document Intelligence (Offline)

## 🚀 Objective
This challenge involves parsing PDF documents to extract structured information. The goal is to build an **offline-compatible**, fast, and CPU-efficient solution that:
- Parses all PDFs in the `input/` directory.
- Extracts meaningful sections based on content structure.
- Outputs results as structured JSON in the `output/` directory.
- Uses a Sentence Transformer model for embedding and ranking sections.
- Completes the full analysis within **60 seconds**.

## 🗂 Folder Structure

```
challenge1a/
├── input/                  # Folder with input PDF files
├── output/                 # Folder where JSON output files will be saved
├── model/                  # Contains locally downloaded SentenceTransformer model
├── main.py                 # Entry point for the pipeline
├── download.py             # Script to download the model before building image
├── utils/
│   ├── parser.py           # Extract text and structure from PDFs
│   ├── ranker.py           # Embedding + scoring logic
│   └── helpers.py          # Utility functions
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image definition
└── README.md               # Project description and instructions
```

## ⚙️ Installation

### 1. Download model locally
Run this first to download and save the embedding model:

```bash
python download.py
```

### 2. Build Docker Image
Make sure your model is inside `model/` directory before building.

```bash
docker build -t challenge1a .
```

### 3. Run the container
Place PDF files in the `input/` directory. Then:

```bash
docker run --rm -v "$PWD/input:/app/input" -v "$PWD/output:/app/output" challenge1a
```

## 🧠 Key Features
- **Offline Execution**: No internet dependency after setup
- **Efficient Embeddings**: Uses `all-MiniLM-L6-v2` (~90MB)
- **PDF to JSON**: Intelligent parsing and structuring
- **Dockerized**: Clean, reproducible execution

## ✅ Output
Each input PDF results in a structured `.json` file inside the `output/` directory with the following format:

```json
{
  "metadata": { "input_file": "example.pdf" },
  "sections": [
    {
      "title": "Executive Summary",
      "content": "....",
      "score": 0.84
    },
    ...
  ]
}
```

## 📌 Notes
- Ensure model is pre-downloaded before building Docker image
- Must complete execution within 60 seconds for all inputs
- CPU-only execution (no GPU used)

---

© Challenge 1A — Adobe Hackathon
