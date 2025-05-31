# app.py
import streamlit as st
import time
import random

# Dummy data to simulate results
sample_articles = [
    {
        "title": "Fed Hikes Interest Rate by 0.25%",
        "source": "Reuters",
        "text": "The Federal Reserve increased interest rates by 25 basis points...",
        "summary": "The Federal Reserve raised interest rates by 0.25% to combat inflation. This may increase borrowing costs for companies like Tesla, potentially reducing consumer demand."
    },
    {
        "title": "China’s GDP Grows Faster Than Expected",
        "source": "Bloomberg",
        "text": "China's economy expanded 6.3% in the last quarter, exceeding expectations...",
        "summary": "China's higher-than-expected GDP growth signals stronger global demand. This could benefit companies with global exposure, such as Tesla."
    },
    {
        "title": "Oil Prices Spike Amid Middle East Tensions",
        "source": "CNBC",
        "text": "Crude oil prices surged past $90 a barrel after conflict in the Middle East escalated...",
        "summary": "Oil prices surged due to geopolitical tensions, potentially increasing production costs for energy-intensive firms like Tesla."
    }
]

# App UI
st.set_page_config(page_title="GenAI News Summarizer", layout="centered")
st.title("📰 GenAI Macro News Summarizer")
st.write("Get macroeconomic summaries for companies or variables using GenAI.")

# Input
company = st.text_input("Enter a Company or Macro Variable (e.g., Tesla, Inflation)", value="Tesla")

if st.button("Fetch News & Summarize"):
    st.info("Searching and summarizing news using GenAI...")
    time.sleep(2)

    # Filter articles (mocked for now)
    filtered_articles = random.sample(sample_articles, k=3)

    st.success(f"Found {len(filtered_articles)} articles related to '{company}'")

    # Display each summary
    for idx, article in enumerate(filtered_articles):
        with st.expander(f"🗞️ {article['title']} - {article['source']}"):
            st.markdown(f"**Full Article:** {article['text']}")
            st.markdown(f"**GenAI Summary:** {article['summary']}")

# Footer
st.markdown("---")
st.caption("🔁 This is a prototype using mock data. GPT integration can be added with OpenAI API.")
