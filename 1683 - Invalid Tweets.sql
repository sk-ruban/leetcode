-- Write your PostgreSQL query statement below
SELECT tweet_id from Tweets
WHERE LENGTH(content) > 15