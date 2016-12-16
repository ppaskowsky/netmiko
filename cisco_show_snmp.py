from netmiko import ConnectHandler
import getpass

username = raw_input("Username: ")
password = getpass.getpass("Password: ")
devices = ['157.132.65.113', '157.132.65.212']

for device in devices:

	net_connect = ConnectHandler(device_type='cisco_ios', ip=device, username=username, password=password) 
	output = net_connect.send_command("show run | section snmp")
	print output
        print '\n=======================\n'

