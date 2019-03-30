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

request3 = "On which days did 1% of the requests lead to an error?"

query3 = (SELECT time::date as day, count(*)
    FROM log
    WHERE status != '200 OK'
    GROUP BY time::date
    ORDER BY count
    DESC limit 1;)


def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results
