import socket
import sys


def get_ip(domain):

    try:
        website_IP = socket.gethostbyname(domain)
        return website_IP
    except:
        return False

if __name__ == "__main__":
    arguments = sys.argv  # uses the commandline argument

    if len(arguments) != 2:
        print("usage: ./domain2ip example.com")
    else:
        host = arguments[1]

        host_ip = get_ip(host)

        if not host_ip:
            print("The website '{0}' does not exist or cannot be found".format(host))
        else:
            print("========================")
            print("the IP is " + host_ip)
            print("========================")
