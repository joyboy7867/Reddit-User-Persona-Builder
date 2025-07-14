from reddit_client import get_reddit_intsance
from urllib.parse import urlparse

def extract_username(url):
    return urlparse(url).path.strip('/').split('/')[-1]

def scrape_user_content(username, limit=10):
    reddit = get_reddit_intsance()
    user = reddit.redditor(username)
    content_list = []
    
    for comment in user.comments.new(limit=limit):
        content_list.append({
            "type": "comment",
            "text": comment.body,
            "permalink": f"https://reddit.com{comment.permalink}"
        })

    for post in user.submissions.new(limit=limit):
        content_list.append({
            "type": "post",
            "text": f"{post.title}\n\n{post.selftext}",
            "permalink": f"https://reddit.com{post.permalink}"
        })

    return {
        "content": content_list,
        "icon_img": getattr(user, "icon_img", None)
    }