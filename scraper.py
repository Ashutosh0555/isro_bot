# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from sentence_transformers import SentenceTransformer





import json

import numpy as np

def get_data():
    # Load all data from multiple JSON files
    with open("missions1.json", "r", encoding="utf-8") as f1, \
         open("missions2.json", "r", encoding="utf-8") as f2, \
         open("mosdac_faq.json", "r", encoding="utf-8") as f3:

        mission1 = json.load(f1)  # list of paragraphs
        mission2 = json.load(f2)  # list of paragraphs
        faq_raw = json.load(f3)   # list of {question, answer}

    # Convert FAQ into question+answer strings
    faq_data = [f"Q: {item['question']}\nA: {item['answer']}" for item in faq_raw]

    # Combine all data
    combined = mission1 + mission2 + faq_data

    # Load SentenceTransformer model and encode
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(combined)

    return combined, embeddings, model
















