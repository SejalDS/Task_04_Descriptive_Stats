# Social Media Political Dataset Analysis

This project analyzes political advertising and post activity on Facebook and Twitter using three coding styles: **Pure Python**, **Polars**, and **Pandas**. Each dataset is processed for statistical summaries and visualized through bar charts, boxplots, and histograms.

---

## 📂 Datasets Used

- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_tw_posts_president_scored_anon.csv`

Each dataset contains advertising or posting data, including impressions, interaction counts, platforms used, and content classification flags.

---

## ▶️ Instructions to Run

1. **Install dependencies**:
   ```bash
   pip install pandas polars matplotlib
   ```

2. **Run the scripts** using Jupyter Notebook, VS Code, or any Python IDE:
   - `.ipynb` notebooks are provided for all approaches.
   - Output files are saved in the same directory as the script.

3. **View Outputs**:
   - CSV files (summary statistics)
   - PNG files (visualizations)

---

## 📊 Code Organization

### 🔹 Pure Python Scripts
- `pure_python_stats_fb_ads.ipynb`
- `pure_python_stats_fb_posts.ipynb`
- `pure_python_stats_tw_posts.ipynb`

### 🔹 Polars Scripts
- `polar_stats_fb_ads.ipynb`
- `polar_stats_fb_posts.ipynb`
- `polar_stats_tw_posts.ipynb`

### 🔹 Pandas Scripts
- `pandas_stats_fb_ads.ipynb`
- `pandas_stats_fb_posts.ipynb`
- `pandas_stats_tw_posts.ipynb`

---

## 📈 Summary of Findings

### 🟦 Facebook Ads
- **Estimated Spend** varies widely: most ads spent under $100, while some exceeded $1,000.
- **Impressions** ranged from a few hundred to several million suggesting varying targeting scopes.
- Most ads used **Facebook** and **Instagram** platforms.
- The most common **currency** was USD, suggesting primary targeting in the U.S.

### 🟩 Facebook Posts
- **Video** and **Photo** post types had the **highest interaction counts**.
- The **U.S.** is the dominant source for political page admins.
- **Interaction totals** ranged significantly some posts achieved over 10,000 engagements.
- Common post sources were consistent with official campaign activity.

### 🟦 Twitter Posts
- **Like**, **Retweet**, and **View** counts showed a long-tail distribution.
- Most tweets originated from **Twitter Web App**, **iPhone**, and tools like **Hootsuite**.
- Content was predominantly in **English**, aligned with U.S.-focused politics.
- Engagement was highly inconsistent indicating a mix of viral vs low-performing tweets.

---

## 📁 Output Files

You will see the following types of outputs:

| File Type         | Description                                        |
|-------------------|----------------------------------------------------|
| `*_summary.csv`   | Descriptive statistics per dataset                 |
| `*_bar_*.png`     | Bar charts for top platforms, countries, etc.      |
| `*_boxplot_*.png` | Boxplots comparing engagement across categories    |
| `*_hist_*.png`    | Histograms of numeric variables                    |

---

## 🧠 Key Tools Used

- Python Standard Library (`csv`, `collections`)
- `pandas` and `polars` for data wrangling
- `matplotlib` for plots and visualizations

---
