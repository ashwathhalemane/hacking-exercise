from socket import *
from itertools import permutations
import time

ip = "165.227.54.122"            #target IP

def Knockports(ports):
    
    for port in ports:
        try:
            print ("[*] Knocking on port: ", port)
            s2 = socket(AF_INET, SOCK_STREAM)
            s2.settimeout(0.1)           # set timeout in 0.1s
            s2.connect_ex((ip, port))
            s2.close()
        
        except (Exception, e):
            print ("[-] %s" % e)


def main():
    
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((ip, 22))              #connect to port 1337 to grab three random ports
    r = [1337,415,2099,921]  
    s.close()

    print ("received: ", r)

    for comb in permutations(r):      # try all the possibility of 3-ports orders 
        print("\n[*] Trying sequence %s" % str(comb))
        Knockports(comb)

    print("[*] Done")


main()
