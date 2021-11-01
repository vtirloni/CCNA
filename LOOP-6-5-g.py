#importando as bibliotecas

import getpass
import sys
import telnetlib

usuario = raw_input ("Entre com o seu usuario: ") #quando chamar a variavel usuario, pega a entrada (printf)
password = getpass.getpass() #quando chamar a variavel password, coleta o password
fileSwitches = open("IP_SWITCHES") #abrir o arquivo criado com os end IP's

for eachSwitch in fileSwitches:   #para cada SW que abrir, vai informar...
    print("Configurando Switch " + str(eachSwitch) + "\n")
    executar_telnet = telnetlib.Telnet(eachSwitch)
    executar_telnet.read_until("Username: ") #quando der telnet no host, vai aguardar ate receber a tela username
    executar_telnet.write(usuario + "\n") #quando receber na tela o username, escrever o usuario, o \n e para forcar e ir pra proxima linha
    if password:
        executar_telnet.read_until("Password: ")
        executar_telnet.write(password + "\n") #o usuario vai digitar a senha e dar um enter

#comandos para executar no equipamento

    executar_telnet.write("conf t\n")

    for n in range (100,200):
        executar_telnet.write("vlan " + str(n) + "\n")
        executar_telnet.write("name VLAN_" + str(n) + "\n")

    executar_telnet.write("end\n")
    executar_telnet.write("write\n")
    executar_telnet.write("exit\n")

    print executar_telnet.read_all() #printa tudo o que foi executado dentro da variavel
