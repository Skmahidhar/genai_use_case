import streamlit as st
import pandas as pd

# Fake data for prototype
data = pd.DataFrame([
    {"Title": "Fed Hikes Interest Rate", "Company": "Tesla", "Summary": "The Fed raised interest rates by 0.25%..."},
    {"Title": "China GDP Beats Forecasts", "Company": "Global Macro", "Summary": "China's economy grew 6% last quarter..."}
])

st.title("GenAI News Summarizer (Prototype)")

# Input area
company = st.text_input("Track Company/Keyword (e.g., Tesla, Inflation)", "Tesla")

if st.button("Fetch News & Summarize"):
    st.success(f"Fetching and summarizing latest news for '{company}'...")

# Display results
st.subheader("Latest Summarized News")
st.dataframe(data)

# Summary Viewer
selected = st.selectbox("Select article to view summary", data["Title"])
summary = data[data["Title"] == selected]["Summary"].values[0]
st.markdown(f"**Summary:** {summary}")
