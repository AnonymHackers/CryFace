import time
import subprocess, os
import socket
import sys
from colorama import Fore, Back, Style
os.system("figlet CryFace")
print("Author: https://github.com/AnonymHackers")
print("[help] Lockup all Commands for CryFace")
print("[exit] exit CryFace tool and go back")
while True:
	Command = str(input(f"root@CryFace>"))
	if Command == 'help':
		print("[Lockup.Hoster] Lock Server ip up")
		print("[Lockup.System] Lock Server System")
		print("[Lock.AllInfos] Lock all Server informations")
		print("[Lock.NorInfos] Lock not all infos from Target")
		print("[Lock.OpenPort] Scanning Normal open ports")
		print("[Lock.PortScan] Scanning aggressive open ports")
	elif Command == 'exit':
		break
	elif Command == 'Lockup.Hoster':
		Target = str(input(f"root@TargetServer>"))
		Tar = socket.gethostbyname(Target)
		print("[=======Lockup.Hoster=======] //CryFace")
		print("Server url: "+Target)
		print("Server ip: "+Tar)
		print("[=======Lockup.Hoster=======] //CryFace")
	elif Command == 'Lockup.System':
		Target = str(input(f"root@TargetServer>"))
		os.system("nmap -O "+Target)
	elif Command == 'Lock.AllInfos':
		Target = str(input(f"root@TargetServer>"))
		print("[INFO] Scanning Target: "+Target)
		os.system("nmap "+Target)
	elif Command == 'Lock.NorInfos':
		Target = str(input(f"root@TargetUrl>"))
		os.system("nikto --url "+Target)
	elif Command == 'Lock.OpenPort':
		Target = str(input(f"root@TargetServer>"))
		os.system("nmap -v -A "+Target)
	elif Command == 'Lock.PortScan':
		Target = str(input(f"root@TargetServer>"))
		os.system("nmap -A "+Target)
	else:
		print("[INFO] Invalid Command: "+Command)