#!/usr/bin/python
import sys
import subprocess
import socket
import ipaddress
import time


def help():
    print("-h Affiche ce message")
    print("-p Ping incompatible avec -sp & -sd")
    print("-sp Ping les ports via socket incompatible avec -p & -sd")
    print("-sd Ping les sous domaines incompatible avec -sp & -p")
    print("-o N'affiche pas le retour dans le cli mais dans des fichiers")
    exit()

def ping(export,addr,fichier):
        p = subprocess.run('ping -n 1 -w 1 '+str(addr),stdout=subprocess.PIPE,shell=True)
        if (p.returncode == 0):
            if(export):
                fichier.write("L'ip "+str(addr)+" a repondu\n")
            else:
                print("")
                print('\033[2;32m'+str(addr)+' \033[0;0m')
                #print("L'ip "+str(addr)+" a repondu")
        else:
            if(export):
                fichier.write("L'ip "+str(addr)+" n'a pas repondu\n")
            #else:
                #print("L'ip "+str(addr)+" n'a pas repondu\n")
                #print('\033[2;31m'+str(addr)+' \033[0;0m',end="")

def socket_ping(export,addr,fichier):
    #ports=[20,21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    ports=[22,2910]
    for i in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.2)
        if sock.connect_ex((str(addr),i))  == 0:
            if(export):
                fichier.write("Le port "+str(i)+" est ouvert sur l'ip "+(str(addr))+"\n")
            else:
                #print("Ping de "+(str(addr))+" sur le port "+str(i)+" en cours .... Time : "+str(time.localtime().tm_hour)+"heures "+str(time.localtime().tm_min)+"minutes "+str(time.localtime().tm_sec)+"secondes." )
                #print("Le port "+str(i)+" est ouvert sur l'ip "+(str(addr)))
                print('\033[2;32m'+str(i)+' \033[0;0m', end='')

        #else:
        #    if(export):
        #        fichier.write("Le port "+str(i)+" n'est pas ouvert sur l'ip "+(str(addr))+"\n")
        #    else:
        #        #print("Le port "+str(i)+" n'est pas ouvert sur l'ip "+(str(addr))+"\n")
        #        print('\033[2;31m'+str(i)+' \033[0;0m', end='')
        sock.close()

def sous_domaine(export):
    site = input("Entrez le domaine du site : (par défaut google.fr) ") 
    if site == "":
        site="google.fr"
    fichier = ""
    print("Test des sous domaines de "+site)
    s_dmn=["www","fr","software","test"]
    for i in s_dmn:
        p = subprocess.run('ping -n 1 -w 1 '+str(i)+"."+str(site),stdout=subprocess.PIPE,shell=True)
        if (p.returncode == 0):
            if(export):
                fichier = open("sous_domaine.txt", "a+")
                fichier.write("L'ip "+str(s_dmn)+" a repondu\n")
                fichier.close()
            else:
                print('\033[2;32m'+str(i)+' \033[0;0m',end="")
        else:
            if(export):
                fichier = open("sous_domaine.txt", "a+")
                fichier.write("L'ip "+str(s_dmn)+" n'a pas repondu\n")
                fichier.close()

            else:
                print('\033[2;31m'+str(i)+' \033[0;0m',end="")

def ip_selection(array):
    network = input("Entrez votre réseau à ping avec le cidre : (par défaut 192.168.1.0/24) ") 
    if network == "":
        network="192.168.1.0/24"
    fichier = ""
    second_fichier = ""
    if(array[2] and array[1]):
        fichier = open("ip_online.txt", "a+")
    if(array[3]):
        if(array[1]):
            second_fichier = open("port_open.txt", "a+")
        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #sock.settimeout(10)

    for addr in ipaddress.IPv4Network(network).hosts():
        if(array[2]):
            ping(array[1],addr,fichier)
        if(array[3]):
            print("<---------------"+str(addr)+"---------------> ",end="")
            socket_ping(array[1],addr,second_fichier)
            print("")
        
    if(array[2] and array[1]):
        fichier.close()
    if(array[3] and array[1]):
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
    elif array[2] == 1 and array[3] == 1 or array[2] == 1 and array[4] == 1 or array[4] == 1 and array[3] == 1:
        help()
    elif array[2] == 1 or array[3] == 1:
        ip_selection(array)
    elif array[4] == 1:
        sous_domaine(array[1])
    else:
        help()

if __name__ == "__main__":
    main()
