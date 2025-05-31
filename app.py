import streamlit as st
import pandas as pd

# Sample Data
summaries = [
    {
        "title": "Fed Raises Interest Rate",
        "summary": "The Federal Reserve increased interest rates by 0.25% to address inflation concerns. This may affect borrowing costs.",
        "category": "Monetary Policy",
        "source": "Reuters",
        "fullText": "The full article explains the implications for corporate and consumer lending..."
    },
    {
        "title": "China GDP Beats Forecast",
        "summary": "China's economy grew by 6.3%, exceeding expectations and signaling robust recovery.",
        "category": "Growth",
        "source": "Bloomberg",
        "fullText": "The full article discusses export trends and manufacturing rebound..."
    },
    {
        "title": "Oil Prices Surge",
        "summary": "Oil prices have surged past $90 a barrel amid Middle East tensions, raising concerns on energy costs.",
        "category": "Commodities",
        "source": "CNBC",
        "fullText": "This report dives into OPEC reactions and global supply chain impacts..."
    }
]

# Sidebar Logo
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg", width=100)
st.sidebar.title("GenAI News")

# Page Title
st.title("📰 GenAI Macro News Dashboard")
st.markdown("Get macroeconomic summaries and analytics using GenAI.")

# Search Input
search_query = st.text_input("Search for news by keyword", "")
filtered = [item for item in summaries if search_query.lower() in item['title'].lower()]

# Summary Cards as Expander
st.subheader("Summarized News")
for item in filtered:
    with st.expander(f"{item['title']} - {item['source']}"):
        st.markdown(f"**Summary:** {item['summary']}")
        if st.button(f"Read Full Article - {item['title']}"):
            st.markdown(f"### {item['title']}")
            st.markdown(item['fullText'])

# Convert to DataFrame for plotting
df = pd.DataFrame(summaries)

# Category Breakdown - Bar Chart
st.subheader("📊 Article Category Breakdown")
category_df = df['category'].value_counts().reset_index()
category_df.columns = ['Category', 'Count']
st.bar_chart(category_df.set_index('Category'))

# Source Count - Bar Chart
st.subheader("📈 Article Count by Source")
source_df = df['source'].value_counts().reset_index()
source_df.columns = ['Source', 'Count']
st.bar_chart(source_df.set_index('Source'))

st.caption("🔁 This is a prototype using mock data. GPT/News API integration can be added.")
