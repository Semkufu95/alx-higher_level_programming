#!/usr/bin/python3
'''
A script that lists all states with names starting N from hbtn_0e_0_usa
'''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    # Create a cursor object to interact with db
    db_cursor = db.cursor()
    # Execute query to fetch data
    db_cursor.execute('SELECT * FROM states WHERE name LIKE BINARY "%N%" ORDER BY states.id ASC;')
    # fetch all data
    result = db_cursor.fetchall()
    # print the data through iteration
    for data in result:
        print(data)
    # close the cursor and database
    db_cursor.close()
    db.close()
