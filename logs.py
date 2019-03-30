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

#connect to database and return results

def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

result_1 = get_queryResults(query1)
result_2 = get_queryResults(query2)
result_3 = get_queryResults(query3)

def print_results(query_list):
    for i in range(len(query_list)):
        title = query_list [i] [0]
        res = query_list [i] [1]
        print("\t" "%s - %d" % (title, res) + "views")
    print("\n")


print(request1)
print_results(result_1)
print(request2)
print_results(result_2)
print(request3)
print_results(result_3)
