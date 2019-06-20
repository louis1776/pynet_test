#!/usr/bin/env python

ip_addr = input("Enter an IP address: ")
ip_addr_list = ip_addr.split(".")

for i in ip_addr_list:
    print("{:<12}".format(i))

