#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass
import glob

if __name__ == "__main__":

    verbose = True

    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")

    f = open("crtlist")
    devlist = [d.rstrip() for d in f.readlines()]
    f.close()


    for dev in devlist:
        nc = ConnectHandler(device_type='juniper', ip=dev, username=username, password=password, verbose=verbose)

        # into config mode
        nc.config_mode()

        nc.send_command('delete forwarding-options apply-groups dhcp')
        nc.send_command('delete routing-instances apply-groups dhcp')
        print nc.send_command('show | compare')
        nc.send_command('rollback 0')
        #print "committing..."
        #nc.commit()
        nc.exit_config_mode()
        print "exiting"
        nc.disconnect()
