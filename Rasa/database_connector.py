# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:31:44 2020

@author: Eswar
"""

import mysql.connector
import mysql

def DataUpdate(exercise,stress, goal):
    mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           passwd = "transistor",
           database = "rasa_database"
           )
    
    mycursor = mydb.cursor()
    #sql = "CREATE TABLE Rasa_table(excercise VARCHAR(255), stress VARCHAR(255), goal VARCHAR(255))"
    sql = 'INSERT INTO rasa_health( exercise,stress, goal) VALUES ("{0}", "{1}", "{2}");'.format(exercise, stress, goal)
    #sql =  'INSERT INTO rasa_health( exercise,stress, goal) VALUES ("goal", "stress", "exercise");'
    mycursor.execute(sql)
    
    mydb.commit()
    
    print(mycursor.rowcount, "record inserted.")
    

if __name__ =="__main__":
    DataUpdate("Daily","Medium"," GRE")
