import psycopg2

DBNAME = "news"

request1 = "What are the most popular articles of all time?"

query1 = ( SELECT title, count(*) as views FROM articles
JOIN log
ON articles.slug = substring(log.path, 10)
GROUP BY title ORDER BY views DESC limit 3;
)

request2 = "Who are the most popular authors of all time?"

query2 = (SELECT authors.name, count(*) as views FROM log , articles, authors
WHERE articles.slug = substring(log.path, 10)
AND articles.author = authors.id
GROUP BY authors.name
ORDER BY views DESC;)
