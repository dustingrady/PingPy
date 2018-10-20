#Author: Dustin Grady
#Function: Ping multiple servers for current status
#Status: In Development

import os
import time
import sys
from subprocess import Popen, PIPE

def printLogo():
    print('_____  _             ____        ')
    print('|  _ \(_)_ __   __ _|  _ \ _   _ ')
    print('| |_) | |  _ \ / _` | |_) | | | |')
    print('|  __/| | | | | (_| |  __/| |_| |')
    print('|_|   |_|_| |_|\__, |_|    \__, |')
    print('               |___/       |___/ ')
    print('             Author: Dustin Grady')


#Get server names from listOfServers.txt and add them to a list
with open('testServers.txt') as server:
    serverNames = server.readlines()

#and then check the response...
def checkResponse():
    for i in range (0, len(serverNames)):#Itterate through the server names

        #response = os.system("ping -c 1 " + serverNames[i])#Get new response from host
        proc = Popen(['ping',  '-c1', serverNames[i].strip()], stdout = PIPE, stderr = PIPE)
        proc.communicate()#Wait for process to terminate
        response = proc.returncode

        #print(serverNames[i])#Testing
        #print(response)#Testing

        if response != 0:
            print(serverNames[i].strip() + ' seems to be down')#Strip /n for formatting
        else:
            print(serverNames[i].strip() + ' seems to be up')


while True:
    printLogo()
    checkResponse()#Call check response method infinitely
    time.sleep(2)#Wait a couple of seconds before refreshing again
    os.system('clear')#Clear the console
