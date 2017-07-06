
# install pymysql: pip3 install pymysql
# CREATE TABLE `mytable` (
# `id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
# `created` TIMESTAMP DEFAULT '0000-00-00 00:00:00',
# `updated` TIMESTAMP DEFAULT now() ON UPDATE now(),
# `myfield` VARCHAR(255)
# );

import argparse, pathlib, time, os, pymysql

def insertIntoDB(table, note):
    # Open database connection
    connection = pymysql.connect('localhost', 'root', '8149omkar', 'notes')

    # prepare a cursor object using cursor() method
    cursor = connection.cursor()

    # Prepare SQL query to INSERT a record into the database.
    insertQuery = 'INSERT INTO ' + table + '(note) VALUES ("' + note + '")'
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

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add_note', help = 'Add notes to the database', action = 'store')
    arg = parser.parse_args()
    if(arg.add_note):
        addNote(arg.add_note)
    else:
        print('Dude give some arguments! Type ArgumentParser -h for more details')


def addNote(note):
    # notesFile = pathlib.Path(os.path.expandvars('.notes.txt'))
    # # notesFile = pathlib.Path(os.path.expandvars(os.getenv("HOME") + '/.notes.txt'))
    # # check of file exists
    # if notesFile:
    #     with open(str(notesFile), 'a+') as File:
    #         currentDateAndTime = time.ctime()
    #         File.write(currentDateAndTime + '\n')
    #         File.write(note + '\n')
    #         File.write('\n')

    insertIntoDB('notes', note)

if __name__ == '__main__':
    argumentParser()
