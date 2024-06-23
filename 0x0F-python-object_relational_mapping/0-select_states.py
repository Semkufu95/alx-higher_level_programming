#!/usr/bin/python3
'''
 A script that lists all states in a database
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    # A cursor object to interact with database
    my_cursor = db.cursor()
    # Exeecute a query to fetch data
    my_cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    # fetch all data returned by the query
    data = my_cursor.fetchall()
    # Print each row(line) by iteration
    for line in data:
        print(line)
    # close the cursor and database
    my_cursor.close()
    db.close()
