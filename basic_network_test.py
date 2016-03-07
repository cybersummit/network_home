#!/usr/bin/env python

import socket
import ipgetter
import netifaces as ni
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='basic_network_test.log',
                    filemode='w')


class BasicNetworkTest:

    def __init__(self):
        pass

    @staticmethod
    def get_internal_ip_addresses():
        logging.info("Getting internal IP addresses...")
        interfaces = ni.interfaces()
        ip_addresses = list()
        for interface in interfaces:
            try:
                ip_addresses.append(ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])
            except:
                pass

        if ip_addresses:
            logging.info("The internal IP address(es) is/are {0}".format(ip_addresses))
        else:
            logging.error("Unable to find an internal IP address on any of the NICs.")

        return ip_addresses

    @staticmethod
    def get_external_ip_address():
        logging.info("Getting external IP address...")
        external_ip = None
        try:
            external_ip = ipgetter.myip()
        except:
            pass

        if external_ip:
            logging.info("The external IP address is {0}".format(external_ip))
        else:
            logging.error("Unable to identify the external IP. Do you have internet connectivity?")

        return external_ip

    @staticmethod
    def get_host_name():
        host = socket.gethostname()
        logging.info("The hostname is {0}".format(host))
        return host

    @staticmethod
    def get_logged_in_user():
        logged_in_user = None
        try:
            logged_in_user = os.getlogin()
            logging.info("The logged-in user is {0}".format(logged_in_user))
        except:
            logging.error("Unable to determine the current logged-in user.")

        return logged_in_user

    def print_summary(self):
        print "Host: {0}".format(self.get_host_name())
        print "Interal IP addresses: {0}".format(self.get_internal_ip_addresses())
        print "External IP address: {0}".format(self.get_external_ip_address())
        print "Logged-in user: {0}".format(self.get_logged_in_user())


if __name__ == "__main__":
    basicNetworkTest = BasicNetworkTest()
    basicNetworkTest.print_summary()

