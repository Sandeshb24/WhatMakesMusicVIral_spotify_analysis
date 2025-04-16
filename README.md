Use the datasets from the link given below.
https://www.kaggle.com/datasets/devdope/900k-spotify
What Makes a Song Go Viral? | Spotify Data Analysis Project

This project dives into Spotify's audio features and metadata to explore what truly makes a **song go viral**. Using data analysis and visualization techniques, we examine factors like energy, danceability, positivity, and more to understand the patterns behind popular tracks.

---

Dataset

The dataset contains a rich set of audio and metadata features for various songs, including:

- **Artist(s), Song Title, Genre, Emotion, Album, Release Date**
- **Audio features**: Energy, Danceability, Positiveness, Acousticness, Instrumentalness, etc.
- **Popularity score** (Spotify metric)
- **Contextual tags**: Good for Party, Work, Relaxation, etc.
- **Similarity scores** with other songs



---

 Objective

To identify **key characteristics of viral songs** based on their audio features and metadata. Specifically, we define:
- **Viral Song** → Popularity ≥ 80
- **Non-Viral Song** → Popularity < 80

---

Technologies Used

- **Python**
- **Pandas** for data cleaning
- **Seaborn & Matplotlib** for visualizations
- **Jupyter Notebook / .py scripts** for analysis
- (Optional) Scikit-learn for simple ML classification



 Project Workflow

### 1.  Data Cleaning
- Remove duplicates and handle missing values
- Convert non-numeric columns (like `Explicit`) to numerical values
- Create a new column: `Viral` (1 if popularity ≥ 80, else 0)

### 2.  Exploratory Data Analysis
- KDE plots comparing viral vs non-viral songs for each feature
- Correlation heatmap
- Genre-wise breakdown of viral songs

### 3. (Optional)  Classification Model
- Logistic Regression or Decision Tree
- Predict whether a song will be viral based on its features
- Evaluate with accuracy, precision, recall

---

##  Key Insights

- Viral songs generally show higher **energy** and **danceability**
- High **positiveness** and **low instrumentalness** are often common
- Explicit content slightly correlates with virality in certain genres
- Certain genres dominate the viral space (e.g., Pop, Hip-Hop)
