import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='170923',
    db='test')
cursor = mydb.cursor()

csv_data = csv.reader(file('customers.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO testcsv(names, \
          classes, mark )' \
          'VALUES("%s", "%s", "%s")',
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
