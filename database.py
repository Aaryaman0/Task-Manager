import sqlite3
from tasks import Tasks
from tabulate import tabulate

con = sqlite3.connect('my.db')

curs = con.cursor()

try:
   curs.execute("""CREATE TABLE Tasks (name text PRIMARY KEY, type text, deadline text)""")
except:
   pass

def commands():
    print('All commands must contain a comma-space ", " between arguments')
    print('Type "add" to insert tasks - add, parameter1, parameter2, parameter3')
    print('Type "delete" to delete tasks - delete, parameter1, parameter2, parameter3')
    print('Type "search_name" to search tasks by name  - search_name, name_parameter')
    print('Type "search_type" to search tasks by type  - search_type, type_parameter')
    print('Type "search_deadline" to search tasks by deadline  - search_deadline, deadline_parameter')
    print('Type "update" to update tasks - update, parameter1, parameter2, parameter3, new_parameter1, new_parameter2, new_parameter3')
    print('Type "print" print the table of tasks')
    print('Type "wipe" to clear the table completely')
    print('Type "exit" to exit the program')

def insert_task(task):
    with con:
        curs.execute("INSERT INTO Tasks VALUES (:Name, :type, :deadline)", {'Name': task.name, 'type': task.type, 'deadline': task.deadline})

def find_task_name(name):
    curs.execute("SELECT * FROM Tasks WHERE name = :name", {'name': name})
    myresult = curs.fetchall()
    print(tabulate(myresult, headers=['Name', 'Type', 'Deadline'], tablefmt='fancy_grid'))

def find_task_type(type):
    curs.execute("SELECT * FROM Tasks WHERE type = :type", {'type': type})
    myresult = curs.fetchall()
    print(tabulate(myresult, headers=['Name', 'Type', 'Deadline'], tablefmt='fancy_grid'))

def find_task_deadline(deadline):
    curs.execute("SELECT * FROM Tasks WHERE deadline = :deadline", {'deadline': deadline})
    myresult = curs.fetchall()
    print(tabulate(myresult, headers=['Name', 'Type', 'Deadline'], tablefmt='fancy_grid'))

def delete_task(task):
    with con:
        curs.execute("""DELETE from Tasks WHERE Name = :Name AND type = :type""", {'Name': task.name, 'type': task.type})

def update_task(task, new_task):
    delete_task(task)
    insert_task(new_task)

def print_table():
    curs.execute("SELECT * FROM Tasks")
    myresult = curs.fetchall()
    print(tabulate(myresult, headers=['Name', 'Type', 'Deadline'], tablefmt='fancy_grid'))

def empty_table():
    curs.execute("DELETE FROM Tasks")

def exit_out():
    exit()

def user_input():
    string = str(input("Please enter your commands: ")).strip()
    array = string.split(", ")
    if(array[0] == "add"):
        try:
            insert_task(Tasks(array[1], array[2], array[3]))
        except:
            print("This name already exists in the database, please use a different name")
        user_input()
    elif(array[0] == "search_type"):
        find_task_type(array[1])
        user_input()
    elif(array[0] == "search_name"):
        find_task_name(array[1])
        user_input()
    elif(array[0] == "search_deadline"):
        find_task_deadline(array[1])
        user_input()
    elif(array[0] == "delete"):
        delete_task(Tasks(array[1], array[2], array[3]))
        user_input()
    elif(array[0] == "update"):
        update_task(Tasks(array[1], array[2], array[3]), Tasks(array[4], array[5], array[6]))
        user_input()
    elif(array[0] == "print"):
        print_table()
        user_input()
    elif(array[0] == "wipe"):
        empty_table()
        user_input()
    elif(array[0] == "commands"):
        commands()
        user_input()
    elif(array[0] == "exit"):
        exit()
    else:
        print("This is an invalid command, please enter a valid command")
        print("Type commands to access the list of commands at any point")
        user_input()

def start():
    print("Hello!")
    print("Here is a list of commands for the database")
    print("")
    commands()
    print("Type commands to access it at any point")
    user_input()


start()

con.commit()

con.close()

# Frontend - to be built (maybe)

# from PyQt5 import QtWidgets
# rom PyQt5.QtWidgets import QApplication, QDialog
# from PyQt5.uic import loadUi

# import sys

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