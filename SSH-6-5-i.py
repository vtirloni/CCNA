# -*- coding: utf-8 -*-

import netmiko
from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.100.4',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2) #vai usar o connethandler para o dicionário que atribuimos iosv_l2
output = net_connect.send_command('show ip int brief')
print output

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0'] #lista no python
output = net_connect.send_config_set(config_commands)
print output

for n in range (2,21):
    print "Ciando vlan " + str(n)
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output
