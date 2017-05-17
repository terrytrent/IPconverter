#!/usr/bin/env python
"""
A simple script that converts domains into IP addresses
this script is meant to be used with python 2
written by metr00
"""

import socket           # import the required library
import sys

def IP(domain):         # define the function IP
					
	website_IP = socket.gethostbyname(domain)

	if website_IP != '198.105.244.28':				
		print("========================")
		print("the IP is " + website_IP)
		print("========================")

	elif website_IP == '198.105.244.28':		
		print("website doesn't exist")



while True:        	# to loop the IP function         
	
	host = sys.argv	  # uses the commandline argument
	
	try:		 		    # while loop if error happens
		IP(host)        	# calls the function IP
	except Exception:
		print("usage: ./domain2ip example.com")
		continue

	
