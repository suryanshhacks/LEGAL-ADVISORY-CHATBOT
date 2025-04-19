Built with:
🧠 LangChain (ConversationalRetrievalChain, Ollama, ChromaDB)
🌐 Web scraping (via requests and re)
💬 Streamlit interface
🗃️ Mistral via Ollama for on-device LLM inference

🚀 Features
✅ Live scraping of legal websites and news sources
✅ Conversational Q&A with memory
✅ Custom URL input
✅ Real-time Streamlit web interface

🧩 Project Structure
bash
Copy code
├── app.py                # Streamlit interface
├── main.py               # Backend logic, LangChain chains
├── webscraping.py        # Custom scraper using requests
├── db/                   # Persisted ChromaDB vectors
└── README.md             # This file

🔧 Setup Instructions

1. Install Dependencies

pip install langchain chromadb streamlit requests

If using Ollama:
Install Ollama: https://ollama.com/download
cmd-
ollama run mistral

Make sure Ollama is running in the background (localhost:11434 by default).

2. Run the App

cmd-
streamlit run app.py

🔎 Sample Legal Sources Used
Indian Penal Code - indiacode.nic.in
Indian Kanoon
LiveLaw
Bar & Bench
Legal Bites
Law Times Journal
You can modify the list of URLs in app.py.

📦 How it Works
Scraping: webscraping.py scrapes each URL’s raw HTML and extracts paragraph content.
Embedding & Indexing: main.py uses OllamaEmbeddings to create vector representations and store them in ChromaDB.
Conversational Chain: A ConversationalRetrievalChain combines memory, document retrieval, and QA.
Frontend: Streamlit provides a simple input box and chat display for easy interaction.

🎯 Future Enhancements
🎙️ Voice input/output using SpeechRecognition and pyttsx3
📂 PDF/Docx legal file ingestion
📤 Export chat to PDF
☁️ Deploy on HuggingFace Spaces or Streamlit Cloud
