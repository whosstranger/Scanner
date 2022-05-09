import pyfiglet, sys, socket, signal
from datetime import datetime

def def_handler(sig, frame):
    print("\n\n[!] Going out...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

ascii_banner = pyfiglet.figlet_format("Scanner",width = 200, font = "ogre")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid argument..")

print("-" * 50)
print("Address scanning: " + target)
print("-" * 50 + '\n')

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
            s.close()
    print("\n [!]By WhosStranger... \n")

except socket.gaierror:
    print("\n [!]Cannot resolve the given address")
    sys.exit()

except socket.error:
    print("\n [!]No response")
    sys.exit()
