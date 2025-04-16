# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\Sandesh Bhat\Desktop\ms\Projects\Spotify analytics\spotify_dataset.csv")  # Replace with your actual file name 

# --- 1. BASIC CLEANING ---
# Drop duplicates
df.drop_duplicates(inplace=True)

# Drop rows with missing values in important column
important_cols = ['Popularity', 'Energy', 'Danceability', 'Positiveness', 'Speechiness', 
                  'Liveness', 'Acousticness', 'Instrumentalness', 'Tempo', 'Loudness (db)']
df.dropna(subset=important_cols, inplace=True)

# Handle 'Explicit' column (convert Yes/No or True/False to binary)
if df['Explicit'].dtype == object:
    df['Explicit'] = df['Explicit'].map({'Yes': 1, 'No': 0, 'True': 1, 'False': 0}).fillna(0)

# Create 'Viral' label
df['Viral'] = df['Popularity'].apply(lambda x: 1 if x >= 80 else 0)

# --- 2. EXPLORATORY DATA ANALYSIS ---
features = ['Energy', 'Danceability', 'Positiveness', 'Speechiness', 'Liveness', 
            'Acousticness', 'Instrumentalness', 'Tempo', 'Loudness (db)']

# Compare feature distributions
for col in features:
    plt.figure(figsize=(8, 4))
    sns.kdeplot(df[df['Viral'] == 1][col], label='Viral', fill=True, color='green')
    sns.kdeplot(df[df['Viral'] == 0][col], label='Non-Viral', fill=True, color='red')
    plt.title(f"{col} Distribution in Viral vs Non-Viral Songs")
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- 3. CORRELATION HEATMAP ---
plt.figure(figsize=(10, 8))
sns.heatmap(df[features + ['Viral']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# --- 4. GENRE ANALYSIS (Top genres among viral songs) ---
if 'Genre' in df.columns:
    top_genres = df[df['Viral'] == 1]['Genre'].value_counts().head(10)
    top_genres.plot(kind='bar', color='purple', title='Top Genres in Viral Songs')
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# --- 5. SAVE CLEANED DATA FOR FUTURE USE ---
df.to_csv("cleaned_viral_songs.csv", index=False)

print("Analysis complete. Cleaned data saved as 'cleaned_viral_songs.csv'.")
