import pyfiglet
import sys
import socket
from _datetime import datetime

ascci_banner = pyfiglet.figlet_format("PORT SCANNER ")
print(ascci_banner)
target = input(str("Target IP :  "))
#BANNER

print("_"*50)
print("Scanning Target " + target)
print("Scanning started at " + str(datetime.now()))
print("_"*50)

try:
    #scan every port on the target IP
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #return open port
        result = s.connect_ex((target,port))
        if result == 0:
            print("[+] port {} is open ".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting ")
    sys.exit()
except socket.error:
    print("\ Host is not responding ")
    sys.exit()