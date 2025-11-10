import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="your password")
cr = mydb.cursor()
Q="CREATE DATABASE daily_tasks"
cr.execut(Q)
q1='''create table tasks(
    Task char,
    Day_of_task date)'''
cr.execute(q1)
q2='''create table task_done(
taskdone char
date_of_taskdone date)'''
mydb.commit()
print("Database Initialised")