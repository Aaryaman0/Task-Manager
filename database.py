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

task_1 = Tasks('Math247 A5', 'Assignment', 'June 15')

# con.execute("INSERT INTO Tasks VALUES (:Name, :type, :deadline)", {'Name': task_1.name, 'type': task_1.type, 'deadline': task_1.deadline})

curs.execute("SELECT * FROM Tasks WHERE type = 'Sideproject'")

print(curs.fetchall())

curs.execute("SELECT * FROM Tasks WHERE type = :type", {'type': 'Assignment'})

print(curs.fetchall())

con.commit()

con.close()