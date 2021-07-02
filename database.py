import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from tasks import Tasks
from tabulate import tabulate
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
    print(tabulate(myresult, headers=['Name', 'Type', 'Deadline'], tablefmt='fancy_grid'))
    # curs.execute("SELECT * FROM Tasks")
    # myresult = curs.fetchall()
    # for x in myresult:
    #    print(x)

def exit_out():
    exit()

task_1 = Tasks('Math247 A5', 'Assignment', 'June 15')
task_2 = Tasks('Math247 A6', 'Assignment', 'June 29')

# insert_task(task_2)
# delete_task(task_2)
print_table

def user_input():
    print("Here is a list of commands for the database")
    print("")
    # print("Type commands to access it at any point")
    string = str(input("Please enter your commands: ")).strip()
    array = string.split(", ")
    print(array)
    print(array[0])
    if(array[0] == "add"):
        insert_task(Tasks(array[1], array[2], array[3]))
        user_input()
    elif(array[0] == "search"):
        find_task(array[1])
        user_input()
    elif(array[0] == "delete"):
        delete_task(Tasks(array[1], array[2], array[3]))
        user_input()
    elif(array[0] == "update"):
        update_task(Tasks(array[1], array[2], array[3]), array[3])
        user_input()
    elif(array[0] == "print"):
        print_table()
        user_input()
    elif(array[0] == "exit"):
        exit()
    else:
        print("This is an invalid command, please enter a valid command")
        user_input()

    
# print_table()

user_input()

# con.execute("INSERT INTO Tasks VALUES (:Name, :type, :deadline)", {'Name': task_1.name, 'type': task_1.type, 'deadline': task_1.deadline})

# curs.execute("SELECT * FROM Tasks WHERE type = 'Sideproject'")

# print(curs.fetchall())

# curs.execute("SELECT * FROM Tasks WHERE type = :type", {'type': 'Assignment'})

# print(curs.fetchall())

#print_table()

con.commit()

con.close()