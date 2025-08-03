import os
import glob
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

# Automatically find the CSV file in the current directory
csv_files = glob.glob('*.csv')
if not csv_files:
    st.error('No CSV file found in the current directory.')
    st.stop()
file_path = csv_files[0]

# Load data
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(file_path)

st.title("📊 Sentiment Analysis Interactive Dashboard")
st.markdown(f"**Data Source:** `{file_path}` | **Rows:** {len(df)}")

# Sidebar filters
st.sidebar.header("Filter Data")
topics = st.sidebar.multiselect("Select Topic(s)", options=sorted(df['Topic'].unique()), default=list(df['Topic'].unique()))
platforms = st.sidebar.multiselect("Select Platform(s)", options=sorted(df['Platform'].unique()), default=list(df['Platform'].unique()))
sentiments = st.sidebar.multiselect("Select Sentiment(s)", options=sorted(df['Sentiment'].unique()), default=list(df['Sentiment'].unique()))

# Filter data
df_filtered = df[
    df['Topic'].isin(topics) &
    df['Platform'].isin(platforms) &
    df['Sentiment'].isin(sentiments)
]

st.markdown(f"### Filtered Data: {len(df_filtered)} rows")
st.dataframe(df_filtered.head(100), use_container_width=True)

col1, col2 = st.columns(2)

# Sentiment Distribution
with col1:
    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df_filtered, x='Sentiment', order=df_filtered['Sentiment'].value_counts().index, ax=ax)
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Polarity Score Distribution
with col2:
    st.subheader("Polarity Score Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df_filtered['PolarityScore'], bins=30, kde=True, ax=ax)
    ax.set_xlabel('Polarity Score')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Sentiment by Platform
st.subheader("Sentiment by Platform")
fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(data=df_filtered, x='Platform', hue='Sentiment', ax=ax)
ax.set_xlabel('Platform')
ax.set_ylabel('Count')
ax.legend(title='Sentiment')
st.pyplot(fig)

# Polarity Score by Topic
st.subheader("Polarity Score by Topic")
fig, ax = plt.subplots(figsize=(10, 4))
sns.boxplot(data=df_filtered, x='Topic', y='PolarityScore', ax=ax)
ax.set_xlabel('Topic')
ax.set_ylabel('Polarity Score')
plt.xticks(rotation=45)
st.pyplot(fig)

# Correlation Heatmap
st.markdown('---')
st.header('Correlation Analysis')
st.markdown('''
**Correlation analysis** helps you understand the relationships between numeric features in your data. A correlation close to 1 or -1 means a strong relationship, while a value near 0 means little or no relationship. In this dataset, only PolarityScore is numeric, but if you add more numeric columns (e.g., Engagement, Likes), they will appear here.
''')
st.subheader('Correlation Heatmap (Numeric Columns)')
numeric_cols = df_filtered.select_dtypes(include='number')
if not numeric_cols.empty:
    fig, ax = plt.subplots(figsize=(4, 3))
    corr = numeric_cols.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig)
else:
    st.info('No numeric columns for correlation heatmap.')

# Map Visualization by Country
st.subheader("Sentiment by Country (Map)")
country_sentiment = df_filtered.groupby(['Country', 'Sentiment']).size().reset_index(name='Count')
country_total = df_filtered.groupby('Country').size().reset_index(name='Total')
country_sentiment = country_sentiment.merge(country_total, on='Country')
country_sentiment['Percent'] = country_sentiment['Count'] / country_sentiment['Total'] * 100

fig = px.choropleth(
    country_sentiment,
    locations='Country',
    locationmode='country names',
    color='Percent',
    hover_name='Country',
    hover_data=['Sentiment', 'Count', 'Percent'],
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Sentiment Distribution by Country',
    labels={'Percent': '% of Sentiment'}
)
st.plotly_chart(fig, use_container_width=True)

# Sentiment Distribution by Country (Bar Chart)
st.subheader('Sentiment Distribution by Country')
sentiment_country = df_filtered.groupby(['Country', 'Sentiment']).size().reset_index(name='Count')
fig = px.bar(sentiment_country, x='Country', y='Count', color='Sentiment', barmode='group', title='Sentiment Count by Country')
st.plotly_chart(fig, use_container_width=True)

# Average Polarity Score by Country
st.subheader('Average Polarity Score by Country')
avg_polarity_country = df_filtered.groupby('Country')['PolarityScore'].mean().reset_index()
fig = px.bar(avg_polarity_country, x='Country', y='PolarityScore', color='PolarityScore', color_continuous_scale='RdYlGn', title='Average Polarity Score by Country')
st.plotly_chart(fig, use_container_width=True)

# Sentiment Breakdown by Country and Platform (Stacked Bar)
st.subheader('Sentiment Breakdown by Country and Platform')
breakdown = df_filtered.groupby(['Country', 'Platform', 'Sentiment']).size().reset_index(name='Count')
fig = px.bar(breakdown, x='Country', y='Count', color='Sentiment', facet_col='Platform', barmode='stack', title='Sentiment by Country and Platform')
st.plotly_chart(fig, use_container_width=True)

# Final Insights
st.markdown("---")
st.markdown("""
#### Final Insights
- Sentiment distribution shows the overall mood of the data.
- Polarity Score distribution gives an idea of sentiment intensity.
- Sentiment breakdown by platform reveals which platforms are more positive/negative.
- Polarity Score by topic highlights which topics are more polarizing.
- Correlation heatmap (if available) shows relationships between numeric features.
""") 