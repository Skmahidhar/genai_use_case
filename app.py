import streamlit as st
import pandas as pd
import plotly.express as px

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

# Summary Cards as Slider
st.subheader("Summarized News")
for item in filtered:
    with st.expander(f"{item['title']} - {item['source']}"):
        st.markdown(f"**Summary:** {item['summary']}")
        if st.button(f"Read Full Article - {item['title']}"):
            st.markdown(f"### {item['title']}")
            st.markdown(item['fullText'])

# Convert to DataFrame for plotting
df = pd.DataFrame(summaries)

# Pie Chart - Category Breakdown
st.subheader("📊 Article Category Breakdown")
category_counts = df['category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']
fig_pie = px.pie(category_counts, values='Count', names='Category', title='Distribution by Category')
st.plotly_chart(fig_pie, use_container_width=True)

# Bar Chart - Source Count
st.subheader("📈 Article Count by Source")
source_counts = df['source'].value_counts().reset_index()
source_counts.columns = ['Source', 'Count']
fig_bar = px.bar(source_counts, x='Source', y='Count', title='Articles per News Source')
st.plotly_chart(fig_bar, use_container_width=True)

st.caption("🔁 This is a prototype using mock data. GPT/News API integration can be added.")
