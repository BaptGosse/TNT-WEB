from serial import *
import time

serialConnexion = None
waitClick = False

def serialInitialization(port, baud):
    global serialConnexion
    serialConnexion = Serial(port, baud)

def serialStop():
    global serialConnexion
    if serialConnexion and serialConnexion.is_open:
        serialConnexion.close()

def changeChannel(currentChannel, futurChannel):
    global serialConnexion
    global waitClick
    waitClick = True
    try:
        while currentChannel != futurChannel:
            if currentChannel < futurChannel:
                command = f"SRVOCONTROL01:{90}\n"
                serialConnexion.write(command.encode())
                time.sleep(0.5)
                command = f"SRVOCONTROL01:{0}\n"
                serialConnexion.write(command.encode())
                currentChannel += 1
                time.sleep(0.5)
            elif currentChannel > futurChannel:
                command = f"SRVOCONTROL02:{90}\n"
                serialConnexion.write(command.encode())
                time.sleep(0.5)
                command = f"SRVOCONTROL02:{0}\n"
                serialConnexion.write(command.encode())
                currentChannel -= 1
                time.sleep(0.5)
    except :
        print("ERROR IN SERIAL UTIL AT CHANGECHANNEL")
    return currentChannel
    waitClick = False