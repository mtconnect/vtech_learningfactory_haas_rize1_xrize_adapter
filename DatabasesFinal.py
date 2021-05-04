import requests,datetime,re

from threading import Timer, Thread
from xml.etree import ElementTree as ET
from xml.dom import minidom
import urllib3
import time

def MTConnectXMLSearch():
    tag = str()#may need to change
    for i in range(20):
        try: 
            response = requests.get("http://mtconnect.mazakcorp.com:5612/current")
        except requests.exceptions.ConnectionError:
            print("Connection Error retrying in " + str(sleeptime) + " secs")
            print(str(i)+"th time trying reconnection")
            time.sleep(sleeptime)
            continue
        except requests.exceptions.MissingSchema:
            print("Missing Schema retrying in " + str(sleeptime) + " secs")
            time.sleep(sleeptime)   
            print(str(i)+"th time trying reconnection")
            continue
        else: 
            break
    else: 
        raise Exception('Unreconverable Error')

    root = ET.fromstring(response.content)
    tag = root.tag.split('}')[0]+'}'#may need to change

    rotary_velocity = root.find(".//"+tag+"DeviceStream")
    rotary_velocity_text = float(rotary_velocity[2][0][5].text)
    print(rotary_velocity[2][0][5].tag, rotary_velocity_text)

    rotary_velocity_timestamp = rotary_velocity[2][0][5].attrib['timestamp']
    print(rotary_velocity_timestamp)

    

"""

###When the execution state is ACTIVE, we want to collect the data that weve defined
### Figure out each of those and how to connect to MTconnect (those meaning FEED, IDLE, ACTIVE for Haas)

Columns = 

    x_val = root.find(".//"+tag+"DeviceStream")
   x_val = float(x_val[4][0][2].text)
    print(x_val)
    xw_val = x_val = root.find(".//"+tag+"DeviceStream")
    xw_val = float(x_val[4][0][3].text)
    print(xw_val)

    y_val = root.find(".//"+tag+"DeviceStream")
   y_val = float(y_val[5][0][2].text)
   print(y_val)
    yw_val = root.find(".//"+tag+"DeviceStream")
    y_wval = float(y_val[5][0][3].text)
    print(yw_val)

    z_val = root.find(".//"+tag+"DeviceStream")
    z_val = float(z_val[6][0][2].text)
    print(z_val)
    zw_val = root.find(".//"+tag+"DeviceStream")
    zw_val = float(z_val[6][0][3].text)
    print(zw_val)
    database_write(rotary_velocity,x_val,y_val,z_val,xw_val,yw_val,zw_val)
"""
#Main infinite searching loop
MTConnectXMLSearch()
