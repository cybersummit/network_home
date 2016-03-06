# Network-TEst.py
import socket
import time
import telnetlib
get local machine name
host = socket.gethostname()
print host
#TODO Fix getaddrinfo syntax
#ip = socket.getaddrinfo ()
# print ip
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='basic_network_test.log',
                    filemode='w')


class BasicNetworkTest:

    def __init__(self):
        pass

    def do_test(self):
        logging.info("Running tests...")

    def __del__(self):
        pass

if __name__ == "__main__":
    basicNetworkTest = BasicNetworkTest()
    basicNetworkTest.do_test()

