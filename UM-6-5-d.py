#importando as bibliotecas

import getpass
import sys
import telnetlib

host = "10.10.100.2" #criando uma varivel host com o IP do SW
usuario = raw_input ("Entre com o seu usuario: ") #quando chamar a variavel usuario, pega a entrada (printf)
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


print executar_telnet.read_all() #printa tudo o que foi executado dentro da variavel
