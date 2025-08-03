# 📊 Sentiment Analysis Project

A data analysis project to explore and visualize sentiment data across platforms and topics using Python and Streamlit.

---

## 📁 Data Overview

- **Source file:** Automatically detected CSV in the project directory  
- **Columns:**
  - `Date`
  - `Topic`
  - `Platform`
  - `Sentiment`
  - `PolarityScore`
- **Total Rows:** 5000

---

## 🧠 Methodology

1. **Data Loading & Inspection**
   - Loaded the CSV file using `pandas`
   - Checked for missing values and dropped incomplete rows (none found)
2. **Summary Statistics**
   - Descriptive statistics generated for all relevant columns
3. **Visualizations**
   - Sentiment distribution
   - Polarity score distribution
   - Sentiment by platform
   - Polarity score by topic
   - Correlation heatmap (numeric fields)
4. **Interactive Dashboard**
   - Built using **Streamlit** for Power BI-like interactivity
   - Filters available: Topic, Platform, Sentiment
   - Dynamic, responsive charts and tables

---

## 📈 Key Visualizations

### 1. Sentiment Distribution  
![Sentiment Distribution](images/sentiment_distribution.png)  
*Distribution of sentiment labels across the dataset*

### 2. Polarity Score Distribution  
![Polarity Score Distribution](images/polarity_score_distribution.png)  
*Histogram showing the spread and intensity of sentiment polarity scores*

### 3. Sentiment by Platform  
![Sentiment by Platform](images/sentiment_by_platform.png)  
*Sentiment breakdown per platform—positive, negative, and neutral*

### 4. Polarity Score by Topic  
![Polarity Score by Topic](images/polarity_by_topic.png)  
*Boxplot showing how polarizing or neutral each topic is*

### 5. Correlation Heatmap  
![Correlation Heatmap](images/correlation_heatmap.png)  
*Correlation matrix for numeric values (only PolarityScore available)*

---

## 🔍 Final Insights

- **Sentiment distribution** shows "Positive" is the most common sentiment.
- **Polarity score** ranges from -1 (negative) to 1 (positive), indicating sentiment strength.
- **Sentiment by platform** identifies which platforms have more favorable or critical discussions.
- **Topic-wise polarity** highlights topics with more emotional or neutral reactions.
- **Correlation** is limited to PolarityScore in this dataset.

---

## 🚀 How to Run

1. **Install required packages**  
  pip install -r requirements.txt
2. **Launch the dashboard** 
  streamlit run sentiment_dashboard.py
. **Explore static outputs**  
- Check the `images/` folder for quick reference visualizations.

---

## 📌 Note

This report and dashboard were generated automatically as part of a data analysis project.
