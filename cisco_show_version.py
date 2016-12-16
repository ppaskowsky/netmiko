from netmiko import ConnectHandler
import getpass

username = raw_input("Username: ")
password = getpass.getpass("Password: ")

testrouter = {'device_type': 'cisco_ios', 'ip': '157.132.65.113', 'username': username, 'password': password} 
testswitch = {'device_type': 'cisco_ios', 'ip': '157.132.65.212', 'username': username, 'password': password} 

all_devices= [testrouter, testswitch]

for device in all_devices:

	net_connect = ConnectHandler(**device) 
	output = net_connect.send_command("show version")
	print output

