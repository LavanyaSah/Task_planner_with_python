#Basically this is a python and my sql integrated project which will help us to store and manage our daily tasks 
import datetime
import mysql.connector as sq
import random as rd
con=sq.connect(host="localhost", user="root", password="xyz", database="daily_tasks")
cr=con.cursor()
def add_task():
    task=input ("enter the task to do:")
    day=input("enter the day when to accomplish the following task(yyyy-mm-dd):")
    print("Adding the task to the list..............")
    q = ("insert into tasks (Task,Day_of_task) values(%s,%s)")
    data = (task,day)
    cr = con.cursor()
    cr.execute(q, data)
    print("Task added........")
    con.commit()
def show_tasks():
    dates=input("Enter the day of which tasks you want to see (yyyy-mm-dd):")
    value=(dates,)
    cr.execute("select*from tasks where Day_of_task = %s",(value))
    rows=cr.fetchall()
    for row in rows:
        print(row)
def task_done():
    done_task=input("enter the task which is done:")
    Date_of_done=input("enter the date of task done(yyyy-mm-dd):")
    q = ("insert into task_done (Taskdone,Day_of_task) values(%s,%s)")
    data = (done_task, Date_of_done)
    cr = con.cursor()
    cr.execute(q, data)
    qu=("delete from tasks where task = done_task")
    try :
        cr.execute(qu)
        cr.commit()
        print("Row removed sucessfully")
        print("Task marked as done and removed from pending list.")
    except cr.Error as err:
        print("Error")
def taskdone_in_interval():
    start_date=("enter the starting date:")
    end_date=("enter the ending date:")
    q= ("SELECT * FROM your_table WHERE date_column BETWEEN %s AND %s ORDER BY date_column ASC")
    cr.execute(q,( start_date, end_date))
    rows= cr.fetchall()
    for row in rows:
        print(row)
        cr.close()
def edit_task():
    old_task = input("Enter the task you want to edit: ")
    new_task = input("Enter the new task description: ")
    new_date = input("Enter the new date (yyyy-mm-dd): ")
    q =("UPDATE tasks SET Task = %s, Day_of_task = %s WHERE Task = %s")
    cr.execute(q, (new_task, new_date, old_task))
    con.commit()
    print("Task updated successfully.")
def show_today_tasks():
    today = datetime.date.today().strftime('%Y-%m-%d')
    cr.execute("SELECT * FROM tasks WHERE Day_of_task = %s", (today,))
    rows = cr.fetchall()
    print(f"Tasks for today ({today}):")
    for row in rows:
        print(row)
def user_interface():
    print("PRESS 1- For showing present day's tasks.")
    print("PRESS 2- For entering present day's tasks done.")
    print("PRESS 3- For showing the tasks done between entered days.")
    print("PRESS 4- For adding the new task to do that day.")
    print("PRESS 5- For editing task:")
    print("PRESS 6- For showing today's tasks:")
    num=int(input("Enter your choice:"))
    if num==4:
        add_task()
    elif num==1:
        show_tasks()
    elif num==2:
        task_done()
    elif num==3:
        taskdone_in_interval()
    elif num==5:
        edit_task()
    elif num==6:
        show_today_tasks()
# login screen
a = rd.randint(1, 9)
b = rd.randint(1, 9)
c = rd.randint(1, 9)
d = rd.randint(1, 9)
e = rd.randint(1, 9)
num = str(a) + str(b) + str(c) + str(d) + str(e)

print("\t\t", num)
n = int(input("Enter The Number Shown Above : "))
if str(n) == num:
    print("               WELCOME THIS PROJECT IS MADE FOR THE TASKS MANAGEMENT")
    user_interface()




