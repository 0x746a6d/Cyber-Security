# 




#imports
import sys
import socket
# imports a funky banner in big letters!
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Haha Deez Nuts")
print(ascii_banner)

# specify the target
ip = 'X.X.X.X' #put IP here! 
# empty ports array to be populated
open_ports =[] 

# ports that will be probed, can also specify specific ones
ports = range(1, 65535)

# tries to connect to the port
def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result

# for loop that iterates through the specified port list
for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")
