import logging
from datetime import datetime
from typing import Optional
from praw import Reddit


logger = logging.Logger(__name__)


class RedditClient:

    client: Reddit

    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        self.client = Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
    
    def get_hot_submissions(self, subreddit: str, limit: Optional[int]=None):
        logger.info(f'Fetching hot submissions for subreddit: {subreddit}')
        try:
            submissions = self.client.subreddit(subreddit).hot(limit=limit)
            for sub in submissions:
                yield {
                    'id': sub.id,
                    'created_utc': datetime.utcfromtimestamp(sub.created_utc),
                    'author': str(sub.author),
                    'subreddit': str(sub.subreddit),
                    'score': sub.score,
                    'title': sub.title,
                    'url': sub.url,
                    'selftext': sub.selftext,
                    'num_comments': sub.num_comments,
                    'upvote_ratio': sub.upvote_ratio,
                    'stickied': sub.stickied
                }
        except Exception as e:
            logger.error('Failed to fetch reddit submissions')
            raise e
