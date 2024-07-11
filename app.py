# app.py

import streamlit as st
from textblob import TextBlob

# CSS to style the background and centralize the heading
st.markdown(
    """
    <style>
    .top-background {
        background-color: #f0f0f0;
        height: 25vh;
        width: 100%;
        position: absolute;
        top: 0;
        z-index: -1;
    }
    .center-heading {
        text-align: center;
        margin-top: 10vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a top background div
st.markdown('<div class="top-background"></div>', unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="center-heading">Content Summarizer and Sentiment Analysis</h1>', unsafe_allow_html=True)

    # Step 1: Create two buttons
    action = st.radio("Choose an action", ("Upload content", "Enter URL"))

    if action == "Upload content":
        # Step 2: Large text field with 500 words max limit
        content = st.text_area("Enter your content (max 500 words):", max_chars=2500, height=200)
        if st.button("Submit"):
            if len(content.split()) > 500:
                st.error("Content exceeds 500 words limit.")
            else:
                summary, sentiment = process_content(content)
                display_results(summary, sentiment)
    
    elif action == "Enter URL":
        # Step 3: Single form field for the URL with a button named "Summary"
        url = st.text_input("Enter the URL:")
        if st.button("Summary"):
            if url:
                content = fetch_content_from_url(url)  # Placeholder function
                summary, sentiment = process_content(content)
                display_results(summary, sentiment)
            else:
                st.error("Please enter a valid URL.")

def process_content(content):
    # Simulate summarization and sentiment analysis
    summary = summarize_content(content)  # Placeholder function
    sentiment = analyze_sentiment(content)
    return summary, sentiment

def summarize_content(content):
    # Placeholder for summary logic (using the first 100 words as summary)
    words = content.split()
    return ' '.join(words[:100])

def analyze_sentiment(content):
    blob = TextBlob(content)
    sentiment_score = blob.sentiment.polarity
    sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    return sentiment

def display_results(summary, sentiment):
    st.subheader("Summary")
    st.write(summary)
    st.subheader("Sentiment Analysis")
    st.write(f"Sentiment: {sentiment}")

def fetch_content_from_url(url):
    # Placeholder function to simulate fetching content from a URL
    # Replace this with actual logic to fetch content
    return "Sample content fetched from the URL."

if __name__ == "__main__":
    main()
