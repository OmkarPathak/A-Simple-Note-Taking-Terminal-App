# Author: OMKAR PATHAK

# install pymysql: pip3 install pymysql
# CREATE TABLE `mytable` (
# `id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
# `created` TIMESTAMP DEFAULT '0000-00-00 00:00:00',
# `updated` TIMESTAMP DEFAULT now() ON UPDATE now(),
# `myfield` VARCHAR(255)
# );

import argparse, pathlib, time, os, pymysql

# Constants
DB_TABLE = 'notes'

def insertIntoDB(note):
    # Open database connection
    connection = pymysql.connect('localhost', 'root', '8149omkar', 'notes')
    # prepare a cursor object using cursor() method
    cursor = connection.cursor()
    # Prepare SQL query to INSERT a record into the database.
    insertQuery = 'INSERT INTO ' + DB_TABLE + '(note) VALUES ("' + note + '")'
    try:
       # Execute the SQL command
       cursor.execute(insertQuery)
       # Commit your changes in the database
       connection.commit()
    except:
       # Rollback in case there is any error
       connection.rollback()
    # disconnect from server
    connection.close()

def readFromDB():
    # Open database connection
    connect = pymysql.connect('localhost', 'root', '8149omkar', 'notes')
    # prepare a cursor object using cursor() method
    cursor = connect.cursor()
    # Prepare SQL query to SELECT all records from the database.
    sql = 'SELECT * FROM ' + DB_TABLE
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          ID = row[0]
          createdAt = row[1]
          modifiedAt = row[2]
          Note = row[3]

          print()
          print('ID:', ID)
          print('Created At:', createdAt)
          print('Last Modified At:', modifiedAt)
          print('Note:', Note)

    except:
       print ("Error: unable to fetch data")

    # disconnect from server
    connect.close()

def modifyData(idx, modifiedNote):
    # Open database connection
    connect = pymysql.connect('localhost', 'root', '8149omkar', 'notes')
    # prepare a cursor object using cursor() method
    cursor = connect.cursor()
    # Prepare SQL query to UPDATE records from the database.
    sql = 'UPDATE ' + DB_TABLE + ' SET note = "' + modifiedNote + '" WHERE id = ' + idx
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       connect.commit()
    except:
       print ("Error: unable to fetch data")
       # Rollback in case there is any error
       connect.rollback()

    # disconnect from server
    connect.close()

def deleteUsingID(idx):
    # Open database connection
    connect = pymysql.connect('localhost', 'root', '8149omkar', 'notes')
    # prepare a cursor object using cursor() method
    cursor = connect.cursor()
    # Prepare SQL query to UPDATE records from the database.
    sql = 'DELETE  FROM ' + DB_TABLE + ' WHERE id = ' + idx
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       connect.commit()
    except:
       print ("Something went wrong try again")
       # Rollback in case there is any error
       connect.rollback()

    # disconnect from server
    connect.close()

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add_note', help = 'Add notes to the database', action = 'store')
    parser.add_argument('-f', '--fetch_all', help = 'Fetch all Records from the database', action = 'store_true')
    parser.add_argument('-u', '--update', nargs = '*', help = 'Update a record from the database', action = 'store')
    parser.add_argument('-d', '--delete', help = 'Delete a record from database', action = 'store')
    arg = parser.parse_args()
    if(arg.add_note):
        insertIntoDB(arg.add_note)
    elif(arg.fetch_all):
        readFromDB()
    elif(arg.update):
        modifyData(arg.update[0], arg.update[1])
    elif(arg.delete):
        deleteUsingID(arg.delete)
    else:
        print('Dude give some arguments! Type ArgumentParser -h for more details')


# def addNote(note):
    # notesFile = pathlib.Path(os.path.expandvars('.notes.txt'))
    # # notesFile = pathlib.Path(os.path.expandvars(os.getenv("HOME") + '/.notes.txt'))
    # # check of file exists
    # if notesFile:
    #     with open(str(notesFile), 'a+') as File:
    #         currentDateAndTime = time.ctime()
    #         File.write(currentDateAndTime + '\n')
    #         File.write(note + '\n')
    #         File.write('\n')



if __name__ == '__main__':
    argumentParser()
