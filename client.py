# RAT Client by Matthew Taylor. Visit matthewaptaylor.github.io for more info.

print"""==========
RAT Client
==========
"""

import socket

HOST = raw_input("IP: ") # The remote host
PORT = 2220 # Default port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = raw_input("CLIENT > ")
    if command.lower() == "help":
        print """SERVER > Help for RAT Client v1.0:
              send <message>                       Sends a message to the server
              logoff                               Logs off the computer
              shutdown                             Shuts down the computer
              restart                              Restarts the computer"""
    else:
        s.sendall(command)

s.close()
