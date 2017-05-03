#!/usr/bin/env python
"""
A simple script that converts domains into IP addresses
this script is meant to be used with python 2
"""

import socket		                                        # import the required library

domain = raw_input("enter the domain you wish to convert: ")    # ask the user for a domain       			
                                              
def IP(domain):
		
	domain = website		
	website_IP = socket.gethostbyname(website)		


	if website_IP != '198.105.244.28':		
		print(website_IP)

	elif website_IP == '198.105.244.28':
		print("website doesn't exist")

