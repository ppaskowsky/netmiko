from netmiko import ConnectHandler
import getpass

username = raw_input("Username: ")
password = getpass.getpass("Password: ")


net_connect = ConnectHandler(device_type='juniper', ip='10.57.32.100', username=username, password=password) 

#enter config mode
net_connect.config_mode()

#send command
net_connect.send_command("set system host-name test3")
print net_connect.send_command("show | compare")


print "committing..."
net_connect.commit()

print "exiting..."
net_connect.exit_config_mode()
net_connect.disconnect()
