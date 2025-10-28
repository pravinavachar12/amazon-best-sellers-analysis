# 📊 Bestseller Books Data Analysis (2009–2019)

Welcome to the **Bestseller Books Data Analysis Project**, a data-driven exploration of the top-selling books from **2009 to 2019**.  
This project leverages **Python**, **Pandas**, and **Matplotlib** to clean, analyze, and visualize patterns in book ratings, genres, and authorship — helping uncover what makes a book a consistent bestseller.

---

## 🧠 Project Overview

The purpose of this project is to:
- Explore and clean a dataset containing bestselling books.
- Analyze trends such as author popularity, price range, and genre ratings.
- Visualize insights using easy-to-read bar charts.
- Export summarized data for further use.

This project demonstrates **data analysis fundamentals** — from loading and cleaning data to generating insights and visuals — ideal for beginners learning **Pandas** and **Matplotlib**.

---

## 🧰 Technologies & Tools Used

| Tool | Purpose |
|------|----------|
| 🐍 **Python** | Programming Language |
| 📘 **Pandas** | Data analysis and manipulation |
| 📊 **Matplotlib** | Data visualization |
| 💾 **CSV Files** | Dataset and output storage |

---

## 📂 Dataset Details

**Dataset Name:** `bestsellers.csv`

**Columns included:**
| Column | Description |
|--------|--------------|
| `Name` | Title of the book |
| `Author` | Name of the author |
| `User Rating` | Average rating of the book |
| `Reviews` | Number of user reviews |
| `Price` | Price of the book (in USD) |
| `Year` | Year the book appeared as a bestseller |
| `Genre` | Type of book (Fiction / Non-Fiction) |

---

## 🚀 How to Run This Project

Follow these steps to set up and run the project on your local machine:

### 1️⃣ Clone the Repository

git clone https://github.com/pravinavachar12/amazon-best-sellers-analysis.git

### 2️⃣ Navigate into the Folder

cd amazon-bestseller-analysis

### 3️⃣ Create a Virtual Environment (Recommended)

python -m venv .venv

### 4️⃣ Activate the Virtual Environment

& .venv\Scripts\Activate.ps1

### 5️⃣ Install Required Libraries

pip install pandas matplotlib

### 6️⃣ Run the Script

python main.py

### 7️⃣ View Output

- The terminal will display the first few rows of data, column info, and analysis results.

- You’ll also see two bar charts pop up:

   - 📊 Top 10 Bestselling Authors (2009–2019)

   - 📘 Average Rating by Genre

- A new file top_authors.csv will be created in your project folder.

