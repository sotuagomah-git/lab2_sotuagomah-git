import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    cleaned = []
    try:
        for tweet in tweets:
            if not tweet or not tweet.get('Text', '').strip():
                continue
            if not tweet.get('Likes', '').strip():
                tweet['Likes'] = '0'
            if not tweet.get('Retweets', '').strip():
                tweet['Retweets'] = '0'
            cleaned.append(tweet)
        return cleaned
    except Exception as e:
        print(f"[ERROR] Data cleaning failed: {str(e)}")
        return []

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
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
        print(f"[ERROR] Finding viral post failed: {str(e)}")
        return None

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
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
                if curr < next_val:
                    sorted_tweets[j], sorted_tweets[j + 1] = sorted_tweets[j + 1], sorted_tweets[j]
                    swapped = True
            if not swapped:
                break
        return sorted_tweets
    except (ValueError, Exception) as e:
        print(f"[ERROR] Sorting failed: {str(e)}")
        return []

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    if not tweets or not keyword or not keyword.strip():
        print("[ERROR] Invalid search term!")
        return []
    try:
        search_lower = keyword.lower()
        return [t for t in tweets if search_lower in t.get('Text', '').lower()]
    except Exception as e:
        print(f"[ERROR] Search failed: {str(e)}")
        return []

if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    
    # QUEST 1: Clean data
    print("[CLEANING] Cleaning data...")
    cleaned = clean_data(dataset)
    print(f"[OK] Cleaned tweets: {len(cleaned)}")
    if not cleaned:
        sys.exit(1)
    
    # QUEST 2: Find viral post
    viral_post = find_viral_tweet(cleaned)
    if viral_post:
        print("\nVIRAL POST:")
        print(f"Username: {viral_post.get('Username', 'N/A')}")
        print(f"Likes: {viral_post.get('Likes', 0)}")
        print(f"Text: {viral_post.get('Text', 'N/A')[:100]}...")
    
    # QUEST 3: Top 10 tweets
    sorted_tweets = custom_sort_by_likes(cleaned)
    top_10 = sorted_tweets[:10]
    print("\nTOP 10 MOST LIKED TWEETS:")
    for rank, tweet in enumerate(top_10, 1):
        print(f"#{rank} | {tweet.get('Likes', 0)} likes | {tweet.get('Username', 'N/A')}")
        print(f"    {tweet.get('Text', 'N/A')[:60]}...")
    
    # QUEST 4: Search
    while True:
        search_word = input("\n[SEARCH] Enter search term (or 'quit'): ").strip()
        if search_word.lower() == 'quit':
            print("[EXIT] Goodbye!")
            break
        if not search_word:
            print("[ERROR] Enter a term.")
            continue
        results = search_tweets(cleaned, search_word)
        print(f"[OK] Found {len(results)} tweets")
        if results:
            for i, tweet in enumerate(results[:5], 1):  # Show first 5
                print(f"{i}. @{tweet.get('Username', 'N/A')} | {tweet.get('Likes', 0)} likes")
                print(f"   {tweet.get('Text', 'N/A')[:80]}...")
        else:
            print("No tweets found.")