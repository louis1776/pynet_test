#!/usr/bin/env python

ip_addr = input("Enter an IP address: ")
ip_addr_list = ip_addr.split(".")

for i in ip_addr_list:
    print("{:<12}".format(i))

ip_addr_list[-1] = 0

for i in ip_addr_list:
    b = bin(int(i))
    print(f"Decimal: {i}, Binary: {b}")
