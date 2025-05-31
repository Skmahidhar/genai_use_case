import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Pie Chart - Category Breakdown
st.subheader("📊 Article Category Breakdown")
category_counts = df['category'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig1)

# Bar Chart - Source Count
st.subheader("📈 Article Count by Source")
source_counts = df['source'].value_counts().reset_index()
source_counts.columns = ['Source', 'Count']
fig2, ax2 = plt.subplots()
sns.barplot(x='Source', y='Count', data=source_counts, ax=ax2)
ax2.set_title('Articles per News Source')
st.pyplot(fig2)

st.caption("🔁 This is a prototype using mock data. GPT/News API integration can be added.")
