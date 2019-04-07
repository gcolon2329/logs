import psycopg2

DBNAME = "news"

request1 = "What are the most popular articles of all time?"

query1 = """SELECT articles.title, count(*) AS num
            FROM log, articles
            WHERE log.status='200 OK'
            AND articles.slug = substr(log.path, 10)
            GROUP BY articles.title
            ORDER BY num DESC
            LIMIT 3;"""

request2 = "Who are the most popular authors of all time?"

query2 = """SELECT authors.name, count(*) as views
            FROM log , articles, authors
            WHERE articles.slug = substring(log.path, 10)
            AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY views DESC;"""

request3 = "On which days did 1% of the requests lead to an error?"

query3 = """
    SELECT to_char(day, 'FMMonth DD,YYYY'),
           error_percent
    FROM (SELECT error.day,
                 round((error_count/total_count)*100, 1) AS error_percent
          FROM (SELECT cast(time AS DATE) AS day,
                       cast(count(status) AS DECIMAL) AS error_count
                FROM   log
                WHERE  status LIKE '404%'
                GROUP BY day) AS error,
               (SELECT cast(time AS DATE) AS day,
                       cast(count(status) AS DECIMAL) AS total_count
                FROM   log
                GROUP BY day) AS total
          WHERE error.day = total.day
          ORDER BY error_percent DESC) AS percent
    WHERE error_percent > 1.0;"""
# connect to database and return results


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

print(result_3)


def print_results(query_list):
    for i in range(len(query_list)):
        title = query_list[i][0]
        res = query_list[i][1]
        print("\t" "%s - %d" % (title, res) + "views")
    print("\n")

# print results


print(request1)
print_results(result_1)
print(request2)
print_results(result_2)
print(request3)
print_results(result_3)
# print("\t" + result_3[0][1] + " - " + str(result_3[0][0]) + "%")
