# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:46:05 2021

@author: lilly
"""

import requests,datetime,re

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

#adjustable variables
sleeptime = 5 #time the program sleeps before it searches the MTConnect Client for new values | Should not be less than the update time of MTConnect Client

#functions block
def database_write(par1,par2,par3,par4,par5,par6, par7):
    sql = "INSERT INTO machines1(devicenum, partid, device, status, dataid, time, value) VALUES (%s, %s,%s,%s,%s,%s,%s)" 
    val = (par1,par2,par3,par4,par5,par6, par7)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
    
from datetime import datetime
def convertDate(d): #allows data to stored in mysql table as datetime type
    d = d[:-1]
    new_date = d
    print(new_date)
    return new_date

def MTConnectXMLSearch():
    tag = str()#may need to change
    for i in range(20):
    try: 
        response = requests.get("http://localhost:5000/current")
    except requests.exceptions.ConnectionError :
        print("Connection Error retrying in " + str(sleeptime) + " secs")
        print(str(i)+"th time trying reconnection")
        time.sleep(sleeptime)
        #continue
    except requests.get.MissingSchema:
        print("Missing Schema retrying in " + str(sleeptime) + " secs")
        time.sleep(sleeptime)   
        print(str(i)+"th time trying reconnection") 

    root = ET.fromstring(response.content)
    tag = root.tag.split('}')[0]+'}'#may need to change 

    partid=2 #enter part number here
    
    uuid = root.find(".//"+tag+"DeviceStream")
    uuid = str(uuid.attrib['uuid'])
    print(uuid)
    
    devicenum = 1 #enter device id here, or use uuid to define
    
    status = root.find(".//"+tag+"DeviceStream")
    status= str(status[1][0][0].text) 
    print(status)
    
    timestamp = root.find(".//"+tag+"Header")
    timestamp = str(timestamp.attrib['creationTime'])
    timestamp = convertDate(timestamp) #convert data type
    
    x_val = root.find(".//"+tag+"DeviceStream")
    id_x = str(x_val[4][0][2].attrib['name'])
    if (x_val[4][0][2].text) == "UNAVAILABLE":
        x_val = "UNAVAILABLE" #allow text type in database
    else:
        x_val = float(x_val[4][0][2].text)
    print(x_val, id_x)
    database_write(devicenum, partid, uuid, status, id_x, timestamp, x_val)
    
    xw_val = x_val = root.find(".//"+tag+"DeviceStream")
    id_xw = str(x_val[4][0][3].attrib['name']) 
    if (x_val[4][0][3].text) == "UNAVAILABLE":
        xw_val = "UNAVAILABLE"
    else:
        xw_val = float(x_val[4][0][3].text)
    print(xw_val, id_xw)
    database_write(devicenum, partid, uuid, status, id_xw, timestamp, xw_val)

    y_val = root.find(".//"+tag+"DeviceStream")
    id_y = str(y_val[5][0][2].attrib['name'])
    if (y_val[5][0][2].text) == "UNAVAILABLE":
        y_val = "UNAVAILABLE"
    else:
        y_val = float(y_val[5][0][2].text)
    print(y_val, id_y)
    database_write(devicenum, partid, uuid, status, id_y, timestamp, y_val)
    
    yw_val = y_val = root.find(".//"+tag+"DeviceStream")
    id_yw = str(y_val[5][0][3].attrib['name']) 
    if (y_val[5][0][3].text) == "UNAVAILABLE":
        yw_val = "UNAVAILABLE"
    else:
        yw_val = float(y_val[5][0][3].text)
    print(yw_val, id_yw)
    database_write(devicenum, partid, uuid, status, id_yw, timestamp, yw_val)

    z_val = root.find(".//"+tag+"DeviceStream")
    id_z = str(z_val[6][0][2].attrib['name'])
    if (z_val[6][0][2].text) == "UNAVAILABLE":
        z_val = "UNAVAILABLE"
    else:
        z_val = float(z_val[6][0][2].text)
    print(z_val, id_z)
    database_write(devicenum, partid, uuid, status, id_z, timestamp, z_val)
    
    zw_val = z_val = root.find(".//"+tag+"DeviceStream")
    id_zw = str(z_val[6][0][3].attrib['name'])
    if (z_val[6][0][3].text) == "UNAVAILABLE":
        zw_val = "UNAVAILABLE"
    else:
        zw_val = float(z_val[6][0][3].text)
    print(zw_val, id_zw)
    database_write(devicenum, partid, uuid, status, id_zw, timestamp, zw_val)

#Main infinite searching
while True:
    MTConnectXMLSearch()
    time.sleep(sleeptime)