#!/usr/bin/python3
'''
A script to prevent SQL injection
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    # Create a cursor and execute the query
    my_cursor = db.cursor()
    my_cursor.execute(
        'SELECT * FROM states WHERE name = s% ORDER BY id', (argv[4], ))
    result = my_cursor.fetchall()
    # Reiterate and print results
    for line in result:
        print(line)

    # close the cursor and database
    my_cursor.close()
    db.close()
