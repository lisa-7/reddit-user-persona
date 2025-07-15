# scraper.py
import praw

def get_reddit_instance():
    return praw.Reddit(
        client_id="IvZCH5f8wahu3PoyQJ0BIg",
        client_secret="6TH0g1hnWwhyTKEbSqs4RjLgAh1WvA",
        user_agent="script:reddit-persona:v1.0 (by u/Glum-Abrocoma3114)"
    )

def extract_username_from_url(url):
    return url.rstrip('/').split('/')[-1]

def get_user_content(username, limit=50):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)
    posts, comments = [], []

    try:
        for post in user.submissions.new(limit=limit):
            posts.append({
                "title": post.title,
                "body": post.selftext,  # <-- for prompt builder compatibility
                "url": f"https://reddit.com{post.permalink}"
            })

        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "url": f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching content for {username}: {e}")

    return posts, comments
