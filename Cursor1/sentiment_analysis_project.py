import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Automatically find the CSV file in the current directory
csv_files = glob.glob('*.csv')
if not csv_files:
    raise FileNotFoundError('No CSV file found in the current directory.')
file_path = csv_files[0]

# Create an 'images' directory if it doesn't exist
images_dir = 'images'
os.makedirs(images_dir, exist_ok=True)

# 1. Load the data
df = pd.read_csv(file_path)

# 2. Inspect the data
print('--- First 5 rows ---')
print(df.head())
print('\n--- Info ---')
df.info()
print('\n--- Columns ---')
print(df.columns)

# 3. Handle missing values
print('\n--- Missing Values ---')
print(df.isnull().sum())
df_clean = df.dropna()
print(f'\nRows after dropping missing: {len(df_clean)} (from {len(df)})')

# 4. Summary statistics
print('\n--- Summary Statistics ---')
print(df_clean.describe(include='all'))

# 5. Visualizations
sns.set(style='whitegrid')

# a) Sentiment distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df_clean, x='Sentiment', order=df_clean['Sentiment'].value_counts().index)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'sentiment_distribution.png'))
plt.close()

# b) Polarity Score distribution
plt.figure(figsize=(8, 5))
sns.histplot(df_clean['PolarityScore'], bins=30, kde=True)
plt.title('Polarity Score Distribution')
plt.xlabel('Polarity Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'polarity_score_distribution.png'))
plt.close()

# c) Sentiment by Platform
plt.figure(figsize=(10, 6))
sns.countplot(data=df_clean, x='Platform', hue='Sentiment')
plt.title('Sentiment by Platform')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'sentiment_by_platform.png'))
plt.close()

# d) Polarity Score by Topic
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_clean, x='Topic', y='PolarityScore')
plt.title('Polarity Score by Topic')
plt.xlabel('Topic')
plt.ylabel('Polarity Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'polarity_by_topic.png'))
plt.close()

# 6. Correlation heatmap (only for numeric columns)
numeric_cols = df_clean.select_dtypes(include='number')
if not numeric_cols.empty:
    plt.figure(figsize=(6, 4))
    corr = numeric_cols.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, 'correlation_heatmap.png'))
    plt.close()
else:
    print('No numeric columns for correlation heatmap.')

# 7. Final insights/observations
print('\n--- Final Insights ---')
print('1. Sentiment distribution shows the overall mood of the data.\n'
      '2. Polarity Score distribution gives an idea of sentiment intensity.\n'
      '3. Sentiment breakdown by platform reveals which platforms are more positive/negative.\n'
      '4. Polarity Score by topic highlights which topics are more polarizing.\n'
      '5. Correlation heatmap (if available) shows relationships between numeric features.')
print(f'\nAll plots have been saved in the "{images_dir}" folder.') 