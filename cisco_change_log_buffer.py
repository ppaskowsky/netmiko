from netmiko import ConnectHandler
import getpass

username = raw_input("Username: ")
password = getpass.getpass("Password: ")
devices = ['157.132.65.113']

for device in devices:

	net_connect = ConnectHandler(device_type='cisco_ios', ip=device, username=username, password=password) 
	
	output = net_connect.send_command("show running-config | include logging buffered")
	print output
        print '\n'
	

	if output == 'logging buffered 16384 informational':
		config_commands = ['logging buffered 32768 informational'] 

	else:
		config_commands = ['logging buffered 16384 informational'] 
	
	output = net_connect.send_config_set(config_commands)
	print output
	
	output = net_connect.send_command("show running-config | include logging buffered")
        print output
        print '\n'




