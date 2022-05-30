import os
import random
import subprocess
import pyfiglet
import sys
from termcolor import colored

def ping_scan(ping_ip):             #ping scan function
    try:
        print("\nChecking host ...\n")
        command = ["ping","-c", "3", ping_ip]           #ping commnad
        result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)         #subprocess.call to run the function and print not output on terminal
        if result == 0:         #if host is alive then proceed to whois scan. Along side creating the directory and storing ping results in a txt file 
            print(colored("-------Host is live-------\n", "green"))
            os.mkdir("Simple_Recon_Tool_Results")   #creating folder to store output
            with open("Simple_Recon_Tool_Results/ping_scan_output.txt", 'w') as file_write:
                subprocess.call(command, stdout=file_write)         #writing output to file
            print(colored("-------Ping scan completed-------","green"))
            whois_scan(ping_ip)         #calling next function
    except:
        print(colored("\nError: Host is not live.\n", "red"))

def whois_scan(whois_ip):           #whois_scan function
    print("\nPerforming Whois Scan ...\n")
    try:
        command = ["whois", whois_ip]
        with open("Simple_Recon_Tool_Results/whois_scan_output.txt", 'w') as file_write:
            subprocess.call(command, stdout=file_write)
        print(colored("-------Whois scan completed-------","green"))
        dig_scan(whois_ip)
    except:
        print(colored("Error in whois scan.\n","red"))
        print(colored("Exiting ...\n","red"))


def dig_scan(dig_ip):               #dig_scan function
    print("\nPerforming Dig Scan ...\n")
    try:
        command = ["dig", dig_ip]
        with open("Simple_Recon_Tool_Results/dig_scan_output.txt", 'w') as file_write:
            subprocess.call(command, stdout=file_write)
        print(colored("-------Dig scan completed-------","green"))
        traceroute_scan(dig_ip)
    except:
        print(colored("Error in dig scan.\n","red"))
        print(colored("Exiting ...\n","red"))

def traceroute_scan(tr_ip):         #traceroute_scan function
    print("\nPerforming Traceroute Scan ...\n")
    try:
        command = ["traceroute", tr_ip]
        with open("Simple_Recon_Tool_Results/traceroute_scan_output.txt", 'w') as file_write:
            subprocess.call(command, stdout=file_write)
        print(colored("-------Traeroute scan completed-------","green"))
        nmap_scan(tr_ip)
    except:
        print(colored("Error in traceroute scan.\n","red"))
        print(colored("Exiting ...\n","red"))
        

def nmap_scan(nmap_ip):             #nmap_scan function
    print("\nPerforming Nmap Scan ...\n")
    try:
        command = ["nmap", "-A", "--script=vuln", nmap_ip]
        print(colored("Nmap scan may take upto 5 minute depending upon the host ...\n","blue"))
        with open("Simple_Recon_Tool_Results/nmap_scan_output.txt", 'w') as file_write:
            subprocess.call(command, stdout=file_write)
        print(colored("-------Nmap scan completed-------","green"))
        pwd_out = subprocess.getoutput(["pwd"])
        print(colored(f"\nAll outputs saved in Simple_Recon_Tool_Results folder at {pwd_out}\n","green"))
    except:
        print(colored("\nError in nmap scan.\n","red"))
        print(colored("Exiting ...\n","red"))

#prints banner of the tool
print("---------------------------------------------------------------------------------")
banner = pyfiglet.figlet_format("A SIMPLE RECON TOOL :-)")
print(colored(banner, "green"))
print(colored("- cyberpands","grey"))
print("---------------------------------------------------------------------------------")

#accepting host input from user and calling ping function
try:
    host = sys.argv[1]
    ping_scan(host)
except:
    print(colored("\nERROR - Host required.\n", "red"))
    print(colored("Usage: python3 auto_recon.py [IP or Host]\n","red"))


