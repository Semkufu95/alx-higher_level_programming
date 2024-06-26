#!/usr/bin/python3
'''
A script that takes in argument and displays values in the states
table of hbtn_0e_usa where name matches argment
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)
    # create cursor and execut query
    my_cursor = db.cursor()
    my_cursor.execute(
        '''SELECT *FROM states WHERE name LIKE BINARY "{}"
        ORDER BY states.id ASC'''.format(argv[4]))
    result = my_cursor.fetchall()
    # reiterate the results and print the output
    for line in result:
        print(line)

    # Close the cursor and database
    my_cursor.close()
    db.close()
