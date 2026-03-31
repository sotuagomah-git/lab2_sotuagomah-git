"""
Data Detective - Social Media Analytics Tool
No .sort(), sorted(), or max() functions
"""
import csv
import os

# QUEST 1: THE DATA AUDITOR (Handle Missing Fields)

#  Cleaning the data: Remove tweets missing Text, replace missing Likes/Retweets with 0
def clean_data(tweets):
    """Remove tweets missing Text, replace missing Likes/Retweets with 0."""
    cleaned, removed, fixed = [], 0, 0
    try:
        for tweet in tweets:
            if not tweet or not tweet.get('Text', '').strip():
                removed += 1
                continue
            if not tweet.get('Likes', '').strip():
                tweet['Likes'] = '0'
                fixed += 1
            if not tweet.get('Retweets', '').strip():
                tweet['Retweets'] = '0'
                fixed += 1
            cleaned.append(tweet)
        return cleaned, removed, fixed
    except Exception as e:
        print(f"error! data cleaning failed: {str(e)}")
        return [], 0, 0

#  printing out the viral post and top 10 tweets

def print_audit_report(tweets, removed, fixed):
    print("\n" + "="*70)
    print("QUEST 1: THE DATA AUDITOR - Data Cleaning Report")
    print("="*70)
    print(f"ok, Total tweets: {len(tweets)}")
    print(f"removed Missing Text: {removed}")
    print(f"fixed Missing Likes/Retweets: {fixed}")
    print("="*70 + "\n")


# QUEST 2: THE VIRAL POST (Find the Maximum - NO max() function!)

# Using the custom function to find the tweet with the highest Likes without using max() or sorted()
def find_viral_post(tweets):
    """Find tweet with highest Likes without using max()."""
    if not tweets:
        return None
    try:
        max_tweet, max_likes = tweets[0], int(tweets[0].get('Likes', 0))
        for i in range(1, len(tweets)):
            current_likes = int(tweets[i].get('Likes', 0))
            if current_likes > max_likes:
                max_likes = current_likes
                max_tweet = tweets[i]
        return max_tweet
    except (ValueError, Exception) as e:
        print(f"error! Finding viral post failed: {str(e)}")
        return None

#  Displaying the viral post details in a nice format

def print_viral_post(viral_tweet):
    if not viral_tweet:
        print("error! No viral post found!")
        return
    print("\n" + "="*70)
    print("QUEST 2: THE VIRAL POST - Most Liked Tweet")
    print("="*70)
    print(f"Username: {viral_tweet.get('Username', 'N/A')}")
    print(f"Likes: {viral_tweet.get('Likes', 0)}")
    print(f"Retweets: {viral_tweet.get('Retweets', 0)}")
    print(f"Text: {viral_tweet.get('Text', 'N/A')[:100]}...")
    print("="*70 + "\n")


# QUEST 3: THE ALGORITHM BUILDER (Custom Sort - NO sort() or sorted()!)
def custom_bubble_sort(tweets, descending=True):
    """Bubble Sort without using .sort() or sorted()."""
    if not tweets:
        return []
    try:
        sorted_tweets = [t for t in tweets]
        n = len(sorted_tweets)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                curr = int(sorted_tweets[j].get('Likes', 0))
                next_val = int(sorted_tweets[j + 1].get('Likes', 0))
                should_swap = (descending and curr < next_val) or (not descending and curr > next_val)
                if should_swap:
                    sorted_tweets[j], sorted_tweets[j + 1] = sorted_tweets[j + 1], sorted_tweets[j]
                    swapped = True
            if not swapped:
                break
        return sorted_tweets
    except (ValueError, Exception) as e:
        print(f"error! Sorting failed: {str(e)}")
        return []

#  function for getting the top tweets using the custom bubble sort function.
def get_top_tweets(tweets, n=10):
    """Get top N tweets sorted by Likes."""
    if not tweets:
        return []
    try:
        sorted_tweets = custom_bubble_sort(tweets, descending=True)
        return sorted_tweets[:min(n, len(sorted_tweets))]
    except Exception as e:
        print(f"error! Getting top tweets failed: {str(e)}")
        return []

# displaying the top tweets
def print_top_tweets(top_tweets):
    if not top_tweets:
        print("error! No tweets to display!")
        return
    print("\n" + "="*70)
    print("QUEST 3: THE ALGORITHM BUILDER - Top 10 Most Liked Tweets")
    print("="*70)
    for rank, tweet in enumerate(top_tweets, 1):
        print(f"\n#{rank} | {tweet.get('Likes', 0)} likes | {tweet.get('Username', 'N/A')}")
        print(f"    {tweet.get('Text', 'N/A')[:60]}...")
    print("\n" + "="*70 + "\n")

# Searching for tweets
# QUEST 4: THE CONTENT FILTER (Search & Extract)
def search_tweets(tweets, search_term):
    """Search for tweets containing a word (case-insensitive)."""
    if not tweets or not search_term or not search_term.strip():
        print("error! Invalid search term!")
        return []
    try:
        search_lower = search_term.lower()
        return [t for t in tweets if search_lower in t.get('Text', '').lower()]
    except Exception as e:
        print(f"error! Search failed: {str(e)}")
        return []

#  Printing search results.
def print_search_results(results, search_term):
    print("\n" + "="*70)
    print(f"QUEST 4: THE CONTENT FILTER - Results for '{search_term}'")
    print("="*70)
    print(f"[OK] Found {len(results)} tweets\n")
    if not results:
        print("No tweets found.")
    else:
        for i, tweet in enumerate(results, 1):
            print(f"{i}. @{tweet.get('Username', 'N/A')} | {tweet.get('Likes', 0)} likes")
            print(f"   {tweet.get('Text', 'N/A')[:80]}...\n")
    print("="*70 + "\n")


def load_csv_file(filename):
    """Load CSV file with error handling."""
    if not os.path.exists(filename):
        print(f"error! File '{filename}' not found!")
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                print("error! CSV is empty!")
                return None
            tweets = [row for row in reader if row]
            print(f"ok, Loaded {len(tweets)} tweets")
            return tweets
    except (FileNotFoundError, csv.Error, UnicodeDecodeError) as e:
        print(f"error! Loading failed: {str(e)}")
        return None

#  Main function to execute the program.
def main():
    """Main program execution."""
    print("\n" + "="*70)
    print("SOCIAL MEDIA DATA DETECTIVE")
    print("="*70 + "\n")
    
    tweets = load_csv_file('twitter_dataset.csv')
    if not tweets:
        return
    
    # QUEST 1: Clean data
    print("\n Cleaning data...")
    cleaned, removed, fixed = clean_data(tweets)
    print_audit_report(cleaned, removed, fixed)
    if not cleaned:
        return
    
    # QUEST 2: Find viral post
    viral_post = find_viral_post(cleaned)
    print_viral_post(viral_post)
    
    # QUEST 3: Top 10 tweets
    top_10 = get_top_tweets(cleaned, n=10)
    print_top_tweets(top_10)
    
    # QUEST 4: Search
    while True:
        search_word = input("\n[SEARCH] Enter search term (or 'quit'): ").strip()
        if search_word.lower() == 'quit':
            print("exiting, Goodbye!")
            break
        if not search_word:
            print("error! Enter a term.")
            continue
        results = search_tweets(cleaned, search_word)
        print_search_results(results, search_word)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n exiting, Interrupted by user.")
    except Exception as e:
        print(f"\n error! Critical error: {str(e)}")
