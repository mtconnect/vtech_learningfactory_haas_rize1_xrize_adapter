# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:11:04 2021

@author: lilly
"""

import requests,datetime,re
import random
from random import gauss

from threading import Timer, Thread
from xml.etree import ElementTree as ET
from xml.dom import minidom
import urllib3
import time
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "john",
    passwd = "Skybolt12$",
    database = "MTConnect"
)
mycursor = mydb.cursor()

sleeptime = 5 #time the program sleeps before it searches the MTConnect Client for new values | Should not be less than the update time of MTConnect Client

#functions block
def database_write(par1,par2,par3,par4,par5,par6, par7):
    sql = "INSERT INTO machines1(devicenum, partid, device, status, dataid, time, value) VALUES (%s, %s,%s,%s,%s,%s,%s)" 
    val = (par1,par2,par3,par4,par5,par6, par7)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")


def CreateData():
    #input sample point, should be reset periodically
    x_val = 438.748
    y_val = 276.465
    z_val = 204.91
    bedtemp = 40
    etemp = 40.1 #etemp refers to the extruder temperature

    #establish minimum and maximum parameter values
    max_x = 500
    max_y = 500
    max_z = 250
    max_bt = 50
    max_et = 50
    min_x = 0
    min_y = 0
    min_z = 0
    min_bt = 20
    min_et = 20
    
    #set variable identifiers
    id_x = "Xpos"
    id_y = "Ypos"
    id_z = "Zpos"
    id_bedtemp = "BedTemp"
    id_etemp = "ExtrTemp"
    
    partid=1 #enter part number here
    uuid = "XRIZE"
    devicenum = 2 #can assign directly or automate
    status = "AVAILABLE" #since simulated, assume available if running sim
    timestamp = datetime.datetime.now()
    
    x = random.gauss(0,2) #change these parameters based on reasonable process assumptions
    x_val = x_val + x #adjust value based on randomly generated increment
    x_val = min(x_val, max_x) #check that new value does not exceed maximum
    x_val = max(x_val, min_x) #check that new value is not below minimum    
    database_write(devicenum, partid, uuid, status, id_x, timestamp, x_val)
    
    #repeat process with different random number for each variable
    y = random.gauss(0,2)
    y_val = y_val + y
    y_val = min(y_val, max_y)
    y_val = max(y_val, min_y) 
    database_write(devicenum, partid, uuid, status, id_y, timestamp, y_val)
    
    z = random.gauss(0,2)
    z_val = z_val + z
    z_val = min(z_val, max_z)
    z_val = max(z_val, min_z)
    database_write(devicenum, partid, uuid, status, id_z, timestamp, z_val)
    
    bt = random.gauss(0,2)
    bedtemp = bedtemp + bt
    bedtemp = min(bedtemp, max_bt)
    bedtemp = max(bedtemp, min_bt)
    database_write(devicenum, partid, uuid, status, id_bedtemp, timestamp, bedtemp)
    
    et = random.gauss(0,2)
    etemp = etemp + et
    etemp = min(etemp, max_et)
    etemp = max(etemp, min_et)
    database_write(devicenum, partid, uuid, status, id_etemp, timestamp, etemp)

#Main infinite searching
while True:
    CreateData()
    time.sleep(sleeptime)    



