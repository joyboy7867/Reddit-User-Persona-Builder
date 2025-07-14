import praw
from dotenv import load_dotenv
import os
load_dotenv()

def get_reddit_intsance():
    reddit=praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent="PersonaBuilder/0.1"
    )
    return reddit