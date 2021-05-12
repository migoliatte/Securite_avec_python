#!/usr/bin/python
import sys
import subprocess
import socket
import ipaddress

def help():
    print("Function _ help")

def ping():
    print("Function _ ping")
    network = input("Entrez votre réseau à ping avec le cidre : (par défaut 192.168.1.0/24) ") 
    if network == "":
        network="192.168.1.0/24"

    fichier = open("ip_online_.txt", "a+")
    for addr in ipaddress.IPv4Network(network):
        p = subprocess.run('ping -n 1 -w 1 '+str(addr),stdout=subprocess.PIPE)
        if (p.returncode == 1):
            print("c'est pas passé avec "+str(addr))
        elif(p.returncode == 0):
            print("c'est passé avec "+str(addr))
            fichier.write(str(addr)+"\n")
        else:
            print("WTF avec " + str(addr))
    fichier.close()
    
def socket_ping():
    print("Function _ socket_ping")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ports=[20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    for i in ports:
        result = sock.connect_ex(("192.168.1.16",i))
        print(i)
    if result == 0:
        print("Le port est ouvert")
    else:
        print("fermé")

def export():
    print("Function _ export")

def sous_domaine():
    print("Function _ sous_domaine")

for i in range(0,len(sys.argv)):
    if str(sys.argv[i]) == "-h":
        help()
    elif str(sys.argv[i]) == "-p":
        ping()    
    elif str(sys.argv[i]) == "-sp":
        socket_ping()
    elif str(sys.argv[i]) == "-o":
        export()
    elif str(sys.argv[i]) == "-sd":
        sous_domaine()