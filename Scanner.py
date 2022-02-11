import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Scanner by stranger")
print(ascii_banner)

#Definicion del objetivo

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Argumento invalido")

#Agregar el objetivo como banner

print("*" * 50)
print("Escaneando direccion:" + target)
print("El escaneo comenzo a las:" + str(datetime.now()))
print("*" * 50)

try:
    #Escaneo de puertos de 1 a 65,535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #Resultado de los puertos
        result = s.connect_ex((target,port))
        if result == 0:
            print("Puerto {} is open".format(port))
            s.close()

except KeyboardInterrupt:
    print("\n Saliendo...")
    sys.exit()

except socket.gaierror:
    print("\n No se pudo resolver la dirección dada")
    sys.exit()

except socket.error:
    print("\n La direccion no responde")
    sys.exit()
