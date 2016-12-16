from netmiko import ConnectHandler

net_connect = ConnectHandler(device_type='juniper', ip='10.57.32.100', username='root', password='Juniper') 
output = net_connect.send_command("show version")
print output
