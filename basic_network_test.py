# Network-TEst.py
import socket
import time
import telnetlib
# get local machine name
host = socket.gethostname()
print host
ip = socket.getaddrinfo ()
print ip