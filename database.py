import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from tasks import Tasks
import sys

con = sqlite3.connect('my.db')

curs = con.cursor()

#class MainWindow(QDialog):
#    def __init__(self):
#        super(MainWindow, self).__init__()
#       loadUi("tabletutorial.ui", self)
#        self.tableWidget.setColumnWidth(0, 300)
#        self.tableWidget.setColumnWidth(1, 200)
#        self.tableWidget.setColumnWidth(2, 200)
#        self.tableWidget.setHorizontalHeaderLabels(["Name", "Type", "Deadline"])
#        # self.loaddata()

#app = QApplication(sys.argv)
#mainwindow = MainWindow()
#widget = QtWidgets.QStackedWidget()
#widget.addWidget(mainwindow)
#widget.show()
#try:
 #   sys.exit(app.exec_())
#except:
  #  print("Exiting")

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

def print_table():
    curs.execute("SELECT * FROM Tasks")
    myresult = curs.fetchall()
    for x in myresult:
        print(x)

task_1 = Tasks('Math247 A5', 'Assignment', 'June 15')
task_2 = Tasks('Math247 A6', 'Assignment', 'June 29')

delete_task(task_2)

# con.execute("INSERT INTO Tasks VALUES (:Name, :type, :deadline)", {'Name': task_1.name, 'type': task_1.type, 'deadline': task_1.deadline})

# curs.execute("SELECT * FROM Tasks WHERE type = 'Sideproject'")

# print(curs.fetchall())

# curs.execute("SELECT * FROM Tasks WHERE type = :type", {'type': 'Assignment'})

# print(curs.fetchall())

print_table()

con.commit()

con.close()