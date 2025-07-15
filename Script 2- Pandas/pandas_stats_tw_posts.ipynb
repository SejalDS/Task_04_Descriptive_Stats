{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb1d1cf2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "DATA_FILE = \"2024_tw_posts_president_scored_anon.csv\"\n",
    "\n",
    "# Load data\n",
    "df = pd.read_csv(DATA_FILE)\n",
    "\n",
    "# Identify numeric and non-numeric columns\n",
    "numeric_cols = df.select_dtypes(include='number').columns.tolist()\n",
    "non_numeric_cols = df.select_dtypes(exclude='number').columns.tolist()\n",
    "\n",
    "# Overall numeric summary\n",
    "df[numeric_cols].describe().transpose().to_csv(\"summary_tw_posts_overall_numeric.csv\")\n",
    "\n",
    "#Overall non-numeric summary\n",
    "non_numeric_summary = []\n",
    "\n",
    "for col in non_numeric_cols:\n",
    "    vc = df[col].value_counts(dropna=True)\n",
    "    most_freq = vc.idxmax() if not vc.empty else None\n",
    "    most_freq_count = vc.max() if not vc.empty else None\n",
    "    unique_count = df[col].nunique(dropna=True)\n",
    "\n",
    "    non_numeric_summary.append({\n",
    "        \"column\": col,\n",
    "        \"unique_count\": unique_count,\n",
    "        \"most_frequent\": most_freq,\n",
    "        \"most_freq_count\": most_freq_count\n",
    "    })\n",
    "\n",
    "pd.DataFrame(non_numeric_summary).to_csv(\"summary_tw_posts_overall_non_numeric.csv\", index=False)\n",
    "\n",
    "# Grouped by id\n",
    "grouped_id = df.groupby(\"id\")[numeric_cols].describe()\n",
    "grouped_id.to_csv(\"summary_tw_posts_grouped_id.csv\")\n",
    "\n",
    "#Grouped by id and quoteId — top 10 only\n",
    "top_id_quote = df.groupby([\"id\", \"quoteId\"]).size().sort_values(ascending=False).head(10).index\n",
    "\n",
    "results = []\n",
    "\n",
    "for tid, qid in top_id_quote:\n",
    "    sub_df = df[(df[\"id\"] == tid) & (df[\"quoteId\"] == qid)]\n",
    "    desc = sub_df[numeric_cols].describe().transpose()\n",
    "    desc[\"id\"] = tid\n",
    "    desc[\"quoteId\"] = qid\n",
    "    results.append(desc)\n",
    "\n",
    "pd.concat(results).to_csv(\"summary_tw_posts_grouped_id_quoteId.csv\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
