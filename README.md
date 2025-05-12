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

To identify key characteristics of viral songs** based on their audio features and metadata. Specifically, we define:
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



---

##  Key Insights

- Viral songs generally show higher **energy** and **danceability**
- High **positiveness** and **low instrumentalness** are often common
- Explicit content slightly correlates with virality in certain genres
- Certain genres dominate the viral space (e.g., Pop, Hip-Hop)

Key Output SnapShots:![output_11](https://github.com/user-attachments/assets/09f5e826-f7ea-46a5-a410-714faaeb0594)
![output_10](https://github.com/user-attachments/assets/1b21aec0-9c3b-4c30-9d41-5635d329b5f0)
![output_9](https://github.com/user-attachments/assets/90c7e06c-0ba6-4f4c-9273-c026d1d09cbe)
![output_8](https://github.com/user-attachments/assets/bb7024ed-8f23-471b-9817-6ac3f5555e79)
![output_7](https://github.com/user-attachments/assets/3fa80106-cac5-47b9-a24a-ca0611ace1fa)
![output_6](https://github.com/user-attachments/assets/929e8494-0a16-406f-b3b8-952b5ffbebbf)
![output_5](https://github.com/user-attachments/assets/9ccbaa8b-0f56-461f-82b5-a168c81a0d46)
![output_4](https://github.com/user-attachments/assets/a318edf5-69de-4dae-aaff-b3c955d11dde)
![output_3](https://github.com/user-attachments/assets/9411864f-2d1e-463f-818d-86c498234131)
![output_2](https://github.com/user-attachments/assets/e4daa586-fb5f-4d39-81a4-de46dc4d3ddd)
![output_1](https://github.com/user-attachments/assets/483e188f-c5a9-4e0a-9c17-f159f991afdf)


