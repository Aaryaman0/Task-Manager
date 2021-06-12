import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from tasks import Tasks
import sys

con = sqlite3.connect('my.db')

curs = con.cursor()

# curs.execute("""CREATE TABLE Tasks (name text, type text, deadline text)""")

# curs.execute("INSERT INTO Tasks VALUES ('React Website', 'Sideproject', 'May 12th')")

# con.commit()

def insert_task(task):
    with con:
        curs.execute("INSERT INTO Tasks VALUES (:Name, :type, :deadline)", {'Name': task.name, 'type': task.type, 'deadline': task.deadline})

def find_task(type_name):
    curs.execute("SELECT * FROM Tasks WHERE type = :type", {'type': type_name})
    print(curs.fetchall())

def update_task(task, date):
    with con:
        curs.execute("""UPDATE Tasks SET deadline = :deadline WHERE Name = :Name AND type = :type""", {'Name': task.name, 'type': task.type, 'deadline': date})

def delete_task(task):
    with con:
        curs.execute("""DELETE from Tasks WHERE Name = :Name AND type = :type""", {'Name': task.name, 'type': task.type})


task_1 = Tasks('Math247 A5', 'Assignment', 'June 15')

# con.execute("INSERT INTO Tasks VALUES (:Name, :type, :deadline)", {'Name': task_1.name, 'type': task_1.type, 'deadline': task_1.deadline})

curs.execute("SELECT * FROM Tasks WHERE type = 'Sideproject'")

print(curs.fetchall())

curs.execute("SELECT * FROM Tasks WHERE type = :type", {'type': 'Assignment'})

print(curs.fetchall())

con.commit()

con.close()