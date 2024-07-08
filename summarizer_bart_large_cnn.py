
import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
import tensorflow as tf
import json
import numpy as np
from transformers import pipeline


def fetch_webpage_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'li'])
    text = ' '.join(element.get_text() for element in text_elements)
    return text

def summarize_webpage(url, sentences_count=5):
    html_content = fetch_webpage_content(url)
    text_content = parse_html_content(html_content)
    return text_content


class InferlessPythonModel:
    def initialize(self):
        self.generator = pipeline(
            "summarization",
            model="facebook/bart-large-cnn")

    def infer(self, text):
        pipeline_output = self.generator(text)
        return pipeline_output[0]["summary_text"]

    def finalize(self):
        self.pipe = None

url = "https://medium.com/the-research-nest/explained-transformers-for-everyone-af01cbe600c5"
summary_bart = summarize_webpage(url)
print(summary_bart)