#importando as bibliotecas

import getpass
import sys
import telnetlib

host = "10.10.100.2" #criando uma varivel host com o IP do SW
usuario = raw_input ("Entre com o seu usuario: ") #quando chamar a variavel usuario, pega a entrada (printf)

host_dois = "10.10.32.3"
password = getpass.getpass() #quando chamar a variavel password, coleta o password

executar_telnet = telnetlib.Telnet(host) #dar telnet na variavel host


executar_telnet.read_until("Username: ") #quando der telnet no host, vai aguardar ate receber a tela username
executar_telnet.write(usuario + "\n") #quando receber na tela o username, escrever o usuario, o \n e para forcar e ir pra proxima linha
if password:
    executar_telnet.read_until("Password: ")
    executar_telnet.write(password + "\n") #o usuario vai digitar a senha e dar um enter

#comandos para executar no equipamento

executar_telnet.write("enable\n")
executar_telnet.write("cisco\n")
executar_telnet.write("conf t\n")
executar_telnet.write("interf loop 0\n")
executar_telnet.write("ip address 1.1.1.1 255.255.255.255\n")
executar_telnet.write("end\n")
executar_telnet.write("write\n")
executar_telnet.write("exit\n")


tn_telnet = telnetlib.Telnet(host_dois)

tn_telnet.read_until("Username: ")
tn_telnet.write(usuario + "\n")
if password:
    tn_telnet.read_until("Password: ")
    tn_telnet.write(password + "\n")

#comandos para executar no equipamento 2


tn_telnet.write("enable\n")
tn_telnet.write("cisco\n")
tn_telnet.write("conf t\n")
tn_telnet.write("int loop 0\n")
tn_telnet.write("ip address 2.2.2.2 255.255.255.255\n")
tn_telnet.write("end\n")
tn_telnet.write("write\n")
tn_telnet.write("exit\n")

print executar_telnet.read_all() #printa tudo o que foi executado dentro da variavel
print tn_telnet.read_all()
