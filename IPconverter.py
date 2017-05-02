#!/usr/bin/python
# meant to be used with python 2
import socket


def IP():
		
	website = raw_input("Enter the website: ")		# asks user for a website
	website_IP = socket.gethostbyname(website)		# converts website to IP


	if website_IP != '198.105.244.28':		
		print(website_IP)

	elif website_IP == '198.105.244.28':
		print("website doesn't exist")

IP()