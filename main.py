# Step 1
import pandas as pd
import matplotlib.pyplot as plt  # For data visualization

# Step 2
df = pd.read_csv('bestsellers.csv')

# Step 3
# Explore the dataset
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

# Step 4
# Clean the dataset
df.drop_duplicates(inplace=True)
df["Price"] = df["Price"].astype(float)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Step 5
# Analyze author popularity and average rating
author_counts = df['Author'].value_counts()
print(author_counts)

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Step 6
# Export results
author_counts.head(10).to_csv("top_authors.csv")

# ================================
# ✨ Step 7: Visualization Section
# ================================

# Top 10 authors (bar chart)
top_10_authors = author_counts.head(10)
plt.figure(figsize=(10, 6))
top_10_authors.plot(kind='bar', color='skyblue')
plt.title('Top 10 Bestselling Authors (2009–2019)', fontsize=14, fontweight='bold')
plt.xlabel('Author', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Average rating by genre (bar chart)
plt.figure(figsize=(6, 4))
avg_rating_by_genre.plot(kind='bar', color=['#66c2a5', '#fc8d62'])
plt.title('Average Rating by Genre', fontsize=14, fontweight='bold')
plt.ylabel('Average Rating', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
