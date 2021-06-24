from dataclasses import dataclass
from datetime import datetime


@dataclass
class Submission:
    id: str
    created_utc: datetime
    author: str
    subreddit: str
    score: int
    title: str
    url: str
    selftext: str
    num_comments: int
    upvote_ratio: float
    stickied: bool

    def __str__(self):
        return f'[{self.id}] ({self.score}) {self.title}'