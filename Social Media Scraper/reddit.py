import praw
# https://praw.readthedocs.io/en/stable/
import os
from dotenv import load_dotenv

load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    refresh_token=os.getenv("REFRESH_TOKEN"),
    user_agent="TangyKiwi65",
)

user = reddit.redditor("VikramDebate217")
print("== COMMENTS ==")
for comment in user.comments.new(limit=None):
    print(comment.body)

print("== POSTS ==")
for submission in user.submissions.new(limit=None):
    print(submission.selftext)

import snscrape.modules.reddit as snreddit
# https://github.com/JustAnotherArchivist/snscrape

limit = 10
reddit = []
for item in snreddit.RedditUserScraper("VikramDebate217").get_items():
    if len(reddit) == limit:
        break
    elif type(item) is snreddit.Submission:
        reddit.append("Post: " + item.selftext)
    elif type(item) is snreddit.Comment:
        reddit.append("Comment: " + item.body)

print(reddit)