#!/usr/bin/python
import sys
import subprocess
import socket
import ipaddress
import time

def help():
    print("Function _ help")
    print("-h Affiche ce message")
    print("-p Ping")
    print("-sp Ping les ports via socket")
    print("-o N'affiche pas le retour dans le cli mais dans des fichiers")

def ping(export,addr,fichier):
        p = subprocess.run('ping -n 1 -w 1 '+str(addr),stdout=subprocess.PIPE)
        if (p.returncode == 0):
            if(export):
                fichier.write("L'ip "+str(addr)+" a repondu\n")
            else:
                print("L'ip "+str(addr)+" a repondu")
        #elif(p.returncode == 1):
        #    if(export):
        #        fichier.write("L'ip "+str(addr)+" n'a pas repondu\n")
        #    else:
        #        print("L'ip "+str(addr)+" n'a pas  repondu\n")
    
def socket_ping(export,addr,fichier,sock):
    ports=[20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    #ports=[22,80]
    for i in ports:
        if sock.connect_ex((str(addr),i)) == 0:
            if(export):
                fichier.write("Le port "+str(i)+" est ouvert sur l'ip "+(str(addr))+"\n")
            else:
                print("Ping de "+(str(addr))+" sur le port "+str(i)+" en cours .... Time : "+str(time.localtime().tm_hour)+"heures "+str(time.localtime().tm_min)+"minutes "+str(time.localtime().tm_sec)+"secondes." )
                print("Le port "+str(i)+" est ouvert sur l'ip "+(str(addr)))
        #else:
        #    if(export):
        #        fichier.write("Le port "+str(i)+" n'est pas ouvert sur l'ip "+(str(addr))+"\n")
        #    else:
        #        print("Le port "+str(i)+" n'est pas ouvert sur l'ip "+(str(addr))+"\n")

def sous_domaine():
    print("Function _ sous_domaine")

def ip_selection(array):
    network = input("Entrez votre réseau à ping avec le cidre : (par défaut 192.168.1.0/24) ") 
    if network == "":
        network="192.168.1.0/24"

    if(array[2]):
        fichier = open("ip_online.txt", "a+")
    if(array[3]):
        second_fichier = open("port_open.txt", "a+")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    for addr in ipaddress.IPv4Network(network).hosts():
        #print("<---------------"+str(addr)+"--------------->")
        if(array[2]):
            ping(array[1],addr,fichier)
        if(array[3]):
            socket_ping(array[1],addr,second_fichier,sock)
        

    if(array[2]):
        fichier.close()
    if(array[3]):
        second_fichier.close()

def menu():
    array=[0,0,0,0,0]
    for i in range(0,len(sys.argv)):
        if str(sys.argv[i]) == "-h":
            array[0]=1
        elif str(sys.argv[i]) == "-o":
            array[1]=1
        elif str(sys.argv[i]) == "-p":
            array[2]=1
        elif str(sys.argv[i]) == "-sp":
            array[3]=1
        elif str(sys.argv[i]) == "-sd":
            array[4]=1
    return array

def main():
    array=menu()
    if array[0] == 1:
        help()
        exit()
    elif array[2] == 1 | array[3] == 1:
        ip_selection(array)
    elif array[4] == 1:
        sous_domaine()

if __name__ == "__main__":
    main()