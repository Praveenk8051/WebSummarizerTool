import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt')

def fetch_webpage_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'li'])
    text = ' '.join(element.get_text() for element in text_elements)
    return text

def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join(str(sentence) for sentence in summary)

def summarize_webpage(url, sentences_count=5):
    html_content = fetch_webpage_content(url)
    text_content = parse_html_content(html_content)
    summary = summarize_text(text_content, sentences_count)
    return summary

if __name__ == "__main__":
    url = "https://medium.com/the-research-nest/explained-transformers-for-everyone-af01cbe600c5"
    summary = summarize_webpage(url)
    print(summary)

