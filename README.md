# 🚀 ISRO AI Chatbot (Hackathon Prototype)

A smart chatbot that answers your questions about ISRO missions and MOSDAC data using semantic search and sentence embeddings.

🔗 **Live Demo** : _Coming Soon_  
📁 **GitHub Repo:** https://github.com/Ashutosh0555/isro_bot

---

## 🔧 Features

- ✅ Scrapes real ISRO & MOSDAC data
- 🔍 Uses **sentence embeddings** with **cosine similarity**
- 💬 Interactive UI with **Streamlit**
- 🧠 Built using **Python**, **Sentence Transformers**, and **BeautifulSoup**

---

## 🧠 How It Works

1. Scrapes and stores data from ISRO and MOSDAC mission pages
2. Converts mission data + FAQs into sentence embeddings
3. Accepts user questions and finds **semantic matches**
4. Displays the most relevant answers ranked by similarity

---

## 📦 Tech Stack

- Python 3.10+
- Streamlit
- BeautifulSoup
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Scikit-learn (cosine similarity)
- JSON data storage

---

## ⚙️ How to Run

```bash
# 1. Clone repo
git clone https://github.com/Ashurosh0555/isro_bot
cd isro_bot

# 2. Create virtual environment 
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the app
streamlit run main.py
