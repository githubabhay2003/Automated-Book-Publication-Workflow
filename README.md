# 📚 Automated Book Publication Workflow

A robust AI-driven pipeline for web-based chapter extraction, AI "spinning", multi-phase human review, voice synthesis, semantic versioning, and RL-based reward evaluation.

---

## 🎯 Objective

This project automates the book publishing workflow using AI and human-in-the-loop design. It fetches a chapter from a URL, uses a Large Language Model (LLM) to rewrite and review the text, enables human editing, evaluates with reinforcement learning techniques, and stores versions with semantic search.

---

## 🛠️ Key Features

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| ✅ Web Scraping & Screenshot     | Extracts chapter text and captures page image from Wikisource               |
| 🤖 AI Writer & Reviewer          | Uses FLAN-T5 to "spin" and review chapter content                           |
| 👤 Human-in-the-Loop             | Allows human editing and rewards it using BLEU and readability scores       |
| 🎙️ Voice Agent                  | Reads out final chapter via offline TTS (`pyttsx3`)                        |
| 🧠 ChromaDB Versioning           | Stores each version with semantic embedding for search and tracking        |
| 🧪 RL-Based Reward System        | Computes reward for human edits using NLP metrics                           |
| 🔍 Semantic Search               | Search historical versions for terms or phrases using vector similarity     |

---

## 🌐 Source URL

> Example Chapter:  
> [`https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1`](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1)

---

## 📁 Folder Structure
```
Automated-Book-Publication-Workflow/
├── output/ # All intermediate and final text outputs
├── chroma_storage/ # Vector DB files for ChromaDB
├── pycache/ # Auto-generated Python bytecode (ignored)
├── ai_writer_chunked.py # AI chapter spinner (FLAN-T5)
├── human_editor.py # Human review + RL-based scoring
├── ai_reviewer.py # [Optional] Separate AI reviewer logic
├── chroma_manager.py # Handles ChromaDB versioning & search
├── scrape_and_screenshot.py # Web scraping and screenshot capture
├── voice_agent.py # Text-to-speech voice agent
├── run_scraper.py # Script to run web scraping
├── run_pipeline.py # Master pipeline runner
├── requirements.txt # Python dependencies
└── README.md # 📘 You're here
```


---

## 🔄 Pipeline Overview

```text
Step 1: Scrape chapter from web & screenshot it
Step 2: AI spins chapter (FLAN-T5)
Step 3: AI reviews it (refines further)
Step 4: Human edits are introduced
Step 5: BLEU and readability rewards are computed
Step 6: Final output is read aloud by TTS agent
Step 7: Version is saved to ChromaDB with metadata
Step 8: Semantic search enabled for previous revisions
```
---
## 🚀 Getting Started
1. Clone the Repo
- git clone https://github.com/githubabhay2003/Automated-Book-Publication-Workflow.git
- cd Automated-Book-Publication-Workflow

2. Install Dependencies
pip install -r requirements.txt

3. Run the Workflow
---
## Scrape chapter
python run_scraper.py

## Run AI-human pipeline
python run_pipeline.py

---
## 🧠 Tools & Technologies

| Tool                             | Purpose                                                                       |
|---------------------------------|---------------------------------------------------------------------------------|
| `transformers`                  | FLAN-T5 model for AI text generation                                          |
| `torch`                         | Backend for running models                                                    |
| `nltk`                          | BLEU scoring for human edit quality                                          |
| `textstat`                      | Flesch Reading Ease scoring                                                 |
| `pyttsx3`                       | Offline voice agent                                                         |
| `ChromaDB`                      | Vector DB for versioning/search                                             |
| `duckdb`                        | Storage backend for ChromaDB                                                |
| `Playwright`                    | Web scraping and screenshots                                                |
---
## 📊 RL-Based Reward Metrics
Human edits are evaluated based on:

BLEU Score: How similar the edited text is to the AI's version

Flesch Reading Ease: Measures human readability

Delta Diff: Shows actual line-by-line edits

Reward results are saved to:
📄 output/reward_log.txt

## 🔍 Semantic Search Demo
Example query from the pipeline:
- 🔎 Searching for: 'Karolin'
- Result: v1_final_ai - Chapter where term "Karolin" appears.
- Semantic matching is based on all-MiniLM-L6-v2 embedding model.

##📦 Requirements
```
transformers==4.41.1
torch>=2.0.0
nltk>=3.8.1
textstat>=0.7.3
chromadb>=0.5.0
pyttsx3>=2.90
pandas>=2.0.0
scikit-learn>=1.3.0
duckdb>=0.10.1
sentence-transformers>=2.2.2
```
## 📜 License
- MIT License — for evaluation purposes only.
- ⚠️ This is a test assignment for Soft-Nerve, not a commercial product.

## 🙋 Author
- Abhay Kumar Saini
- GitHub: @githubabhay2003
