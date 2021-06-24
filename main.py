import luigi
import luigi.contrib.postgres
import os
import pandas as pd
from dotenv import load_dotenv
from praw.reddit import Submission

load_dotenv()

class FetchRedditData(luigi.Task):
    subreddit = luigi.Parameter()
    limit = luigi.IntParameter(default=100)
    task_complete = False

    def complete(self):
        return self.task_complete

    def run(self):
        from reddit_client import RedditClient
        from sqlalchemy import create_engine
        reddit = RedditClient(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT')
        )
        engine = create_engine(os.getenv('PG_STRING'))
        data = reddit.get_hot_submissions(self.subreddit, self.limit)
        pd.DataFrame(list(data)).to_sql('submissions', engine, if_exists='append', index=False)
        self.task_complete = True

class DedupRedditData(luigi.Task):
    subreddit = luigi.Parameter()
    limit = luigi.IntParameter(default=100)

    def requires(self):
        return FetchRedditData(self.subreddit, self.limit)

    def run(self):
        from sqlalchemy import create_engine
        engine = create_engine(os.getenv('PG_STRING'))
        with open('sql/reddit_dedup.sql', 'r') as f:
            engine.execute(f.read())

if __name__ == '__main__':
    use_local_scheduler = os.getenv('ENV') == 'DEVELOPMENT'
    luigi.build([
        DedupRedditData(subreddit='wallstreetbets')
    ], local_scheduler=use_local_scheduler)