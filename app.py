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

# Sidebar Branding
st.sidebar.image("https://www.freepik.com/free-vector/cute-grandfather-reading-newspaper-cartoon-vector-icon-illustration-people-education-isolated-flat_70824427.htm#from_element=cross_selling__vector", width=100)
st.sidebar.title("🧓 CynicalCapital")
st.sidebar.caption("where snark meets markets")

# Navigation
page = st.sidebar.radio("Navigate", ["📊 Dashboard", "📄 Article Details"])

# Convert to DataFrame
df = pd.DataFrame(summaries)

if page == "📊 Dashboard":
    # Header
    st.title("📰 CynicalCapital – Daily Snark, Serious Finance")
    st.markdown("Welcome, finance minions. Get your dose of macro insights without the fluff.")

    # Search Bar
    search_query = st.text_input("🔍 Filter by keyword", "")
    filtered = [item for item in summaries if search_query.lower() in item['title'].lower()]

    # Summary Cards
    st.subheader("🧾 Curated Summaries")
    for item in filtered:
        with st.expander(f"{item['title']} | {item['source']}"):
            st.markdown(f"**Date:** {item['date']}")
            st.markdown(f"**Summary:** {item['summary']}")
            st.markdown(f"[Read Full Article]({item['link']})")
            if st.button(f"🔎 Details – ID {item['id']}"):
                st.session_state['selected_article_id'] = item['id']
                st.experimental_rerun()

    # Data Visualizations
    st.subheader("📈 Breakdown by Category")
    category_df = df['category'].value_counts().reset_index()
    category_df.columns = ['Category', 'Count']
    st.bar_chart(category_df.set_index('Category'))

    st.subheader("🗞️ Source Distribution")
    source_df = df['source'].value_counts().reset_index()
    source_df.columns = ['Source', 'Count']
    st.bar_chart(source_df.set_index('Source'))

    st.caption("⚠️ This is a prototype with mock data. Real-time GPT/News API coming soon.")

elif page == "📄 Article Details":
    st.title("📄 Deep Dive")
    if 'selected_article_id' in st.session_state:
        article_id = st.session_state['selected_article_id']
        article = next((item for item in summaries if item['id'] == article_id), None)

        if article:
            st.header(article['title'])
            st.markdown(f"**📅 Date:** {article['date']}")
            st.markdown(f"**📰 Source:** {article['source']}")
            st.markdown(f"**📌 Summary:** {article['summary']}")
            st.markdown(f"**🧠 Full Text:** {article['fullText']}")
            st.markdown(f"[🔗 Original Article]({article['link']})")

            st.subheader("📊 Related Categories")
            st.bar_chart(df['category'].value_counts())
        else:
            st.warning("❌ Article not found.")
    else:
        st.info("👈 Go back and pick an article, banker.")
