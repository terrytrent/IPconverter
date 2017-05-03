#!/usr/bin/env python
"""
A simple script that converts domains into IP addresses
this script is meant to be used with python 2
"""

import socket           # import the required library
      			                                              
def IP(domain):         # define the function IP
		
	domain = website		
	website_IP = socket.gethostbyname(website)		


	if website_IP != '198.105.244.28':		
		print(website_IP)

	elif website_IP == '198.105.244.28':
		print("website doesn't exist")

while True:        # to loop the IP function         
	
	host = raw_input("enter the website you want to convert: ")	#asks for user input
	
	IP(host)        # calls the function IP
	
	choice = raw_input("do you want to convert another website? y/n")
	if choice == 'Y':
		return True

	elif choice == 'y':	
		return True
	
	elif choice == 'N':
		print("goodbye!")
		return False
	
	elif choice == 'n':
		print("goodbye!")
		return False
	
	
			
