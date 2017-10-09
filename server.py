# RAT Server by Matthew Taylor. Visit matthewaptaylor.github.io for more info.
import socket
import subprocess

print"""==========
RAT Server
==========
"""

HOST = "0.0.0.0" # IP address
PORT = 2220 # Default port

print "Connection info:"
print "IP: " + socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "SERVER > Connection made: " + str(addr)
while 1:
    command = conn.recv(1024)
    if not command: break
    if command[:4].lower() == "send":
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
    conn.sendall(command)
conn.close()
