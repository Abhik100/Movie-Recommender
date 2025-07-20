Here’s the `README.md` for my Movie Recommender System project :

# 🎬 Movie Recommender System

A **content-based movie recommendation system** built with Python using NLP and machine learning techniques. It recommends movies based on the similarity of metadata such as genres, keywords, cast, crew, and movie overviews.

---

📌 Overview

This project uses two datasets from [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) — `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`. 
The data is cleaned, processed, and used to create a content-based filtering engine using **CountVectorizer** and **Cosine Similarity**.

---

🚀 Features

* Combines movie metadata (overview, genres, cast, crew, keywords) into a single tag.
* Applies **NLP preprocessing**: tokenization, lowercase conversion, and **stemming** using NLTK.
* Vectorizes tags using `CountVectorizer` (with max 5000 features and English stopwords removal).
* Computes **cosine similarity** between vectors to recommend top 5 similar movies.
* Saves the cleaned and processed data using `pickle`.

---

## 🧰 Tech Stack

* **Python** 🐍
* **Pandas**, **NumPy** – data manipulation
* **Scikit-learn** – vectorization and similarity calculation
* **NLTK** – stemming
* **Pickle** – data serialization

---

 🗂 Dataset Columns Used

* `title`
* `overview`
* `genres`
* `keywords`
* `cast` (top 3 actors)
* `crew` (director only)

---

 🔧 How It Works

1. **Data Merge:** Combine `movies.csv` and `credits.csv` on the movie title.
2. **Data Cleaning:** Remove nulls, duplicates, and parse JSON fields using `ast.literal_eval`.
3. **Feature Extraction:** Extract top 3 cast members and director.
4. **Preprocessing:**

   * Tokenize and stem text.
   * Merge all fields into a single `tags` column.
   * Convert to lowercase and remove spaces in multi-word tags.
5. **Vectorization:** Use `CountVectorizer` to create feature vectors.
6. **Similarity Calculation:** Use `cosine_similarity` to find similar movies.
7. **Recommendation Function:** Input a movie title and return top 5 similar movie titles.

---

 📦 Usage

🔍 Recommend a Movie

```python
recommend('Avatar')
```

**Output:**

```
Titan A.E.
Independence Day
Small Soldiers
Aliens vs Predator: Requiem
Ender's Game
```

 💾 Save the Processed Data

```python
import pickle
pickle.dump(new_df, open('movies.pkl', 'wb'))
```

---

 🧪 Example

Here’s a sample tag for the movie “Avatar” after processing:

```
in the 22nd century a paraplegic marine is dispatch to the moon pandora on a unique mission he become torn between follow his order and protect the world he feel is his home action adventure fantasy sciencefiction cultureclash future spacewar spacecolony samworthington zoesaldana sigourneyweaver jamescameron
```

--
 📁 Files

* `tmdb_5000_movies.csv` – movie metadata
* `tmdb_5000_credits.csv` – cast and crew information
* `movies.pkl` – serialized processed data (optional output)
* `main.py` or Jupyter Notebook – main recommendation code

---
