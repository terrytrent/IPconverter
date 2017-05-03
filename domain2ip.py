#!/usr/bin/env python
"""
A simple script that converts domains into IP addresses
this script is meant to be used with python 2
written by metr00
"""

import socket           													# import the required library
      			                                              
def IP(domain):         													# define the function IP
		
			
	website_IP = socket.gethostbyname(domain)		

	if website_IP != '198.105.244.28':		
		
		print("========================")
		print("the IP is " + website_IP)
		print("========================")

	elif website_IP == '198.105.244.28':
		
		print("website doesn't exist")

while True:        															      # to loop the IP function         
	
	host = raw_input("enter the website you want to convert (ex:'domain.com')\n")	  # asks for user input
	IP(host)        													          # calls the function IP
	choice = raw_input("do you want to convert another website? (y/n): ")
	
	if choice == 'Y' or choice == 'y':
		
		continue

	elif choice == 'N' or choice == 'n':	
		
		print("goodbye!")
		break

	elif choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n':  # this else-if loop is provided if user provides invalid input
																		    # keeps looping till correct input
		while True:

			again = raw_input("invalid input, try again (y/n): ")

			if again == 'Y' or again == 'y':

				break

			elif again == 'N' or again == 'n':

				break
