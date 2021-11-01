#importando as bibliotecas

import getpass
import sys
import telnetlib

host = "10.10.100.2" #criando uma varivel host com o IP do SW
usuario = raw_input ("Entre com o seu usuario: ") #quando chamar a variavel usu$

password = getpass.getpass() #quando chamar a variavel password, coleta o passw$

executar_telnet = telnetlib.Telnet(host) #dar telnet na variavel host


executar_telnet.read_until("Username: ") #quando der telnet no host, vai aguard$
executar_telnet.write(usuario + "\n") #quando receber na tela o username, escre$
if password:
    executar_telnet.read_until("Password: ")
    executar_telnet.write(password + "\n") #o usuario vai digitar a senha e da
   
   
#comandos para executar no equipamento

executar_telnet.write("enable\n")
executar_telnet.write("cisco\n")
executar_telnet.write("conf t\n")

for numerovlans in range (2,149):
    executar_telnet.write("vlan" + str(numerovlans) + "\n")
    executar_telnet.write("name VLAN_" + str(numerovlans) + "\n")

executar_telnet.write("end\n")
executar_telnet.write("write\n")

print executar_telnet.read_all() #printa tudo o que foi executado dentro da var$

