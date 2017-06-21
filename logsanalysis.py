import psycopg2


DBNAME = "news"


# Connects to the database and returns the db and cursor
def connect():
    try:
        db = psycopg2.connect("dbname={}".format(DBNAME))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


# Executes a given query string and prints certain data fields
def get_query_and_print_results(myquery):
    db, cursor = connect()
    cursor.execute(myquery)
    for row in cursor:
        print (row[0], " - ", str(row[1]), "views")
    db.close()


# Executes a given query string and prints certain data fields specific to error data
def get_query_and_print_results_errors(myquery):
    db, cursor = connect()
    cursor.execute(myquery)
    for row in cursor:
        print (row[0], " - ", str(row[1]), "% errors")
    db.close()


if __name__ == '__main__':
    # Execute and print report data #1
    print ("1. What are the most popular three articles of all time?")
    query_1 = get_query_and_print_results("select articles.title, count(*) as views "
                                   "from articles "
                                   "inner join log on log.path like concat('/article/', articles.slug, '%') "
                                   "where log.status = '200 OK' "
                                   "group by articles.title order by views desc limit 3")

    # Execute and print report data#2
    print ("\n2. Who are the most popular article authors of all time?")
    query_1 = get_query_and_print_results("select authors.name, count(*) as views "
                                          "from articles "
                                          "inner join authors on articles.author = authors.id "
                                          "inner join log on log.path like concat('/article/', articles.slug, '%') "
                                          "where log.status = '200 OK' "
                                          "group by authors.name order by views desc")  

    # Execute and print report data #3
    print ("\n2. On which days did more than 1% of requests lead to errors?")
    query_1 = get_query_and_print_results_errors("select to_char(to_date(mdate, 'YYYY-MM-DD'), 'Month DD YYYY') as mdate, errored_requests_percent "
                                          "from (select substring(cast(log.time as text), 0, 11) as mdate "
                                          ", round( 100.0 * sum(case when status = '404 NOT FOUND' then 1 else 0 end) / sum(1), 2) as errored_requests_percent "
                                          "from log "
                                          "group by mdate) as inner_query "
                                          "where errored_requests_percent >=1 "
                                          "order by mdate asc")  
