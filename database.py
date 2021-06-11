import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

con = sqlite3.connect('my.db')

curs = con.cursor()

# curs.execute("""CREATE TABLE Tasks (Name text, type text, deadline text)""")

# curs.execute("INSERT INTO Tasks VALUES ('React Website', 'Sideproject', 'May 12th')")

# con.commit()

curs.execute("SELECT * FROM Tasks WHERE type = 'Sideproject'")

print(curs.fetchall())

con.commit()

con.close()