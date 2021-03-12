#Download Scapy from the interwebs before using
#Import Scapy
import scapy.all as scapy
#Create regular expressions to ensure that the input is correctly formatted
import re

ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_add_range_entered = input("\nPlease enter the ip address and range you want to scan")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break 

#try arping the ip address range supplied by the user
# try arping() method in scapy creates a packet with an ARP message
# and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff
#If a valid ip address range was supplied the program will return the list of all results 
arp_result = scapy.arping(ip_add_range_entered)