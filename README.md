# Data Detective — Social Media Analytics Tool

 
> A lightweight command-line tool for loading, cleaning, ranking, and searching through Twitter/X datasets — built with pure Python and no external libraries.
 
---
 
## 📋 Table of Contents
 
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Constraints](#constraints)
 
---
 
## Overview
 
**Data Detective** is a terminal-based analytics tool that takes a raw CSV of tweets and walks you through four analysis steps — cleaning bad data, surfacing the most viral post, building a top-10 leaderboard, and running live keyword searches.
 
The project is intentionally built without any built-in sorting or comparison functions (`max()`, `sorted()`, `.sort()`), using manual algorithm implementations instead.
 
---
 
## Features
 
-  Automatic data cleaning — removes empty rows, patches missing values
-  Viral post detection — finds the most liked tweet without `max()`
-  Top 10 leaderboard — ranked by likes using a custom Bubble Sort
-  Live keyword search — case-insensitive, runs in a loop
-  Top 5 most active users — via companion Bash script
-  Zero dependencies — only Python's built-in `csv` and `os` modules
 
---
 
## Getting Started
 
### Prerequisites
 
- Python 3.x installed on your machine
- A CSV dataset of tweets (see [CSV Format](#csv-format) below)
 
### Installation
 
```bash
# Clone or download the project
git clone https://github.com/sotuagomah-git/lab2_sotuagomah-git
cd sotuagomah-git
```
 

---
 
## Usage
 
```bash
python data-detective.py
```
 
The program runs automatically through all four steps. At the end, it drops into an interactive search prompt:
 
```
[SEARCH] Enter search term (or 'quit'): python
```
 
Type any keyword to filter tweets. Type `quit` to exit.
 
---
 
## Feed Analyzer Script
 
`feed-analyzer.sh` is a companion Bash script that prints the **top 5 most active users** in the dataset along with how many tweets each one posted.
 
### Prerequisites
 
- Bash (Linux / macOS / WSL on Windows)
- Python 3.x (used internally to parse the CSV safely)
- Standard Unix tools: `cut`, `sort`, `uniq`, `awk`
 
```
 
The left column is the tweet count, the right column is the username.
 
### What the script does internally
 
| Step | Tool | What it does |
|------|------|--------------|
| 1 | `python3` | Reads the CSV and extracts the `Username` column cleanly |
| 2 | `sort` | Groups identical usernames together |
| 3 | `uniq -c` | Counts how many times each username appears |
| 4 | `sort -nr` | Sorts by count, highest first |
| 5 | `head -n 5` | Keeps only the top 5 |
| 6 | `awk` | Formats the output into aligned columns |
 
---
 
 
 
---
 
## Project Structure
 
```
data-detective/
│
├── data-detective.py       # Main Python script
├── feed-analyzer.sh        # Bash script — top 5 most active users
├── twitter_dataset.csv     # Your dataset (not included)
└── README.md               # This file
```
 
---
 
## How It Works
 
The program runs in four sequential steps ("Quests"):
 
### Quest 1 — Handle missing fields
Cleans the raw dataset by removing tweets with no text and filling in any missing `Likes` or `Retweets` values with `0`. Prints a report showing how many rows were removed or fixed.
 
### Quest 2 — Loop through the list to find the tweet with the highest 'Likes'
Finds the tweet with the highest like count using a manual linear scan — iterates through every tweet and tracks the current best, without using `max()`.
 
### Quest 3 —  Implement Bubble Sort or Selection Sort
Sorts all tweets by likes using a hand-written **Bubble Sort** algorithm. Returns the top 10 results as a ranked leaderboard.
 **How the sort works:** It repeatedly steps through the list, compares each pair of adjacent tweets, and swaps them if the one with fewer likes comes first — pushing the most liked tweets to the top with each pass.
 
### Quest 4 — Search for a keyword and extract matching tweets into a new list
Runs an interactive search loop. Accepts a keyword from the user and returns all tweets whose text contains that word (case-insensitive). Repeats until the user types `quit`.
 
---
 
## Constraints
 
This project was built under the following deliberate restrictions:
 
| Banned | Replaced with |
|----------------|------------------------------------------|
| `max()` | Manual loop tracking the highest value |
| `sorted()` | Custom Bubble Sort implementation |
| `.sort()` | Custom Bubble Sort implementation |
 
These constraints exist to demonstrate how Python's built-in functions work under the hood.
 
---
