from __future__ import print_function

import os
import socket
import time
import subprocess


host='engineer@192.168.1.6'
ssh=subprocess.Popen(['ssh', host], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)
print("connected")

''' this is to get into the RIZE printer '''
ssh.communicate('murphyslaw\n')
ssh.communicate('commandline\n')
ssh.communicate('M\n')
ssh.communicate('s 0')
''' this is to read that if there are no more spaces left to continue to the next line '''
for line in ssh.stdout:
    if line=="END\n":
        break
    print(line,end='')     

ssh.communicate(parameter)

'''

from ssh2.session import Session
import ssh2

def communicate(parameter):
    result=""
    channel.execute(parameter)
    time.sleep(1)
    try:
        size, data = channel.read()
        while size > 0:
            result += data.decode("utf-8")
            size, data = channel.read()
    except ssh2.exceptions.Timeout: 
        return result

Credential information

host = '192.168.1.6'
user = 'engineer'

This is to get into the printer and start the session, and password entry

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 22))
session = Session()
session.set_timeout(3000)
session.handshake(sock)
session.userauth_password(
    user, 'murphyslaw')

channel = session.open_session()

This is to display the x position of the printer

result= communicate('commandline\n')
print(result)
result= communicate('M\n')
print(result)
result= communicate('s 0\n')
print(result)

This is to leave the printer
    
#result = communicate('exit')
#print(result)

session.set_timeout(0)
channel.close()
print("Exit status: %s" % channel.get_exit_status())

#x position, y position, z position, bed temperature, extruder temp, extrusion rate

'''
