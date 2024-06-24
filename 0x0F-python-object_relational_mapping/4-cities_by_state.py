#!/usr/bin/python3
'''
List all cities from a data base
'''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    # Create cursor object and query execution
    my_cursor = db.cursor()
    my_cursor.execute(
        '''SELECT cities.id, cities.name, states.name
        FROM cities JOIN states
        ON states.id = cities.state_id ORDER BY cities.id''')
    # Create a variable to fetch data from the query
    result = my_cursor.fetchall()
    # print results by iteration
    for city in result:
        print(city)

    # close the cursor and the database
    my_cursor.close()
    db.close()
