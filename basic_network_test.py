#!/usr/bin/env python

import socket
import ipgetter
import netifaces as ni
import logging

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
        logging.info("Getting IP addresses...")
        interfaces = ni.interfaces()
        ip_addresses = list()
        for interface in interfaces:
            try:
                ip_addresses.append(ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])
            except:
                pass

        return ip_addresses

    @staticmethod
    def get_external_ip_address():
        external_ip = None
        try:
            external_ip = ipgetter.myip()
        except:
            pass

        return external_ip

    @staticmethod
    def get_host_name():
        host = socket.gethostname()
        return host

    def print_summary(self):
        print "Host: {0}".format(self.get_host_name())
        print "Interal IP addressed: {0}".format(self.get_internal_ip_addresses())
        print "External IP address: {0}".format(self.get_external_ip_address())

if __name__ == "__main__":
    basicNetworkTest = BasicNetworkTest()
    basicNetworkTest.print_summary()

