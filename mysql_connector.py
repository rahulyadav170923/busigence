import MySQLdb as dbapi
import sys
import csv

database_list='show databases;';

tables_list='show tables'
column_info='SHOW COLUMNS FROM %s.%s;'

def mysql_options(dbServer,dbPass,dbSchem,dbUser):
    db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
    cur=db.cursor()
    cur.execute(database_list)
    databases=cur.fetchall()
    databases=[i[0] for i in databases]
    options=[]
    for i in databases:
        info={}
        info['database_name']=i[0]
        cur.execute('use %s' % i)
        cur.execute(tables_list)
        tables=cur.fetchall()
        tables=[m for m in result[0]]
        for j in tables:
            table_data={}
            table_data['table_name']=j;
            cur.execute(column_info % (i[0],j))
            column_names=cur.fetchall()
            column_names=[i[0] for i in column_names]
        options.append(info)
    return options


'''
def mysql_to_csv(headers,data):
    with open("mysql_to_csv.csv",'wb') as out_file:
        csv_w = csv.writer(out_file)
        csv_w.writerow(headers)
        for i in data:
            csv_w.writerow([i['text'].encode('utf-8')])

'''










def mysql_to_csv(dbServer,dbPass,dbSchem,dbUser,query_schema):
    db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
    cur=db.cursor()
    for i in query_schema:
        cur.execute(database_list)
    databases=cur.fetchall()









c = csv.writer(open("temp.csv","wb"))
c.writerow(result)
