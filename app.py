import streamlit as st
import pandas as pd
import datetime

# Sample Data
summaries = [
    {
        "id": 1,
        "title": "Fed Raises Interest Rate",
        "summary": "The Federal Reserve increased interest rates by 0.25% to address inflation concerns. This may affect borrowing costs.",
        "category": "Monetary Policy",
        "source": "Reuters",
        "fullText": "The full article explains the implications for corporate and consumer lending...",
        "date": "2025-05-29",
        "link": "https://www.reuters.com/article/fed-rate-hike"
    },
    {
        "id": 2,
        "title": "China GDP Beats Forecast",
        "summary": "China's economy grew by 6.3%, exceeding expectations and signaling robust recovery.",
        "category": "Growth",
        "source": "Bloomberg",
        "fullText": "The full article discusses export trends and manufacturing rebound...",
        "date": "2025-05-28",
        "link": "https://www.bloomberg.com/china-gdp-growth"
    },
    {
        "id": 3,
        "title": "Oil Prices Surge",
        "summary": "Oil prices have surged past $90 a barrel amid Middle East tensions, raising concerns on energy costs.",
        "category": "Commodities",
        "source": "CNBC",
        "fullText": "This report dives into OPEC reactions and global supply chain impacts...",
        "date": "2025-05-30",
        "link": "https://www.cnbc.com/oil-prices-surge"
    }
]

# Sidebar Logo
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg", width=100)
st.sidebar.title("GenAI News")

# Navigation
page = st.sidebar.radio("Go to", ["Dashboard", "Article Details"])

# Shared DataFrame
df = pd.DataFrame(summaries)

if page == "Dashboard":
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
            st.markdown(f"**Date:** {item['date']}")
            st.markdown(f"**Link:** [Read Original Article]({item['link']})")
            if st.button(f"Open Details - {item['id']}"):
                st.session_state['selected_article_id'] = item['id']
                st.experimental_rerun()

    # Charts
    st.subheader("📊 Article Category Breakdown")
    category_df = df['category'].value_counts().reset_index()
    category_df.columns = ['Category', 'Count']
    st.bar_chart(category_df.set_index('Category'))

    st.subheader("📈 Article Count by Source")
    source_df = df['source'].value_counts().reset_index()
    source_df.columns = ['Source', 'Count']
    st.bar_chart(source_df.set_index('Source'))

    st.caption("🔁 This is a prototype using mock data. GPT/News API integration can be added.")

elif page == "Article Details":
    st.title("📄 Article Details")
    if 'selected_article_id' in st.session_state:
        article_id = st.session_state['selected_article_id']
        article = next((item for item in summaries if item['id'] == article_id), None)
        if article:
            st.markdown(f"## {article['title']}")
            st.markdown(f"**Date:** {article['date']}")
            st.markdown(f"**Source:** {article['source']}")
            st.markdown(f"**Summary:** {article['summary']}")
            st.markdown(f"**Full Text:** {article['fullText']}")
            st.markdown(f"🔗 [Visit Original Article]({article['link']})")

            # Chart for Article Context (Dummy Example)
            st.subheader("📊 Related Category Context")
            category_count = df['category'].value_counts()
            st.bar_chart(category_count)
        else:
            st.warning("Article not found.")
    else:
        st.info("Go back and select an article to view details.")
