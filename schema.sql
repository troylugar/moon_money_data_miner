CREATE TABLE submissions (
  "id"              VARCHAR(8) NOT NULL,
  "created_utc"     TIMESTAMP NOT NULL,
  "author"          VARCHAR(50) NOT NULL,
  "subreddit"       VARCHAR(50) NOT NULL,
  "score"           INT NOT NULL,
  "title"           VARCHAR(500) NOT NULL,
  "url"             VARCHAR(500) NOT NULL,
  "selftext"        TEXT,
  "num_comments"    INT NOT NULL,
  "upvote_ratio"    DECIMAL(3,2) NOT NULL,
  "stickied"        BOOLEAN NOT NULL,
  "date_added_utc"  TIMESTAMP NOT NULL DEFAULT timezone('utc', now()),
  "stock_mentioned" VARCHAR(10),
  "guid"            UUID NOT NULL DEFAULT gen_random_uuid()
);