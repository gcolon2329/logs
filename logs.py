import psycopg2

DBNAME = "news"

request1 = "What are the most popular articles of all time?"

query1 = ( SELECT title, count(*) as views FROM articles
JOIN log
ON articles.slug = substring(log.path, 10)
GROUP BY title ORDER BY views DESC limit 3;
)
