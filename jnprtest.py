#!/usr/bin/env python

import json, sys

from ncclient import manager

def connect(host, user, password):
    conn = manager.connect(host=host,
            username=user,
            password=password,
            timeout=10,
            device_params = {'name':'junos'},
            hostkey_verify=False)

    conn.lock()

    vlan = sys.argv[1]
    interface = sys.argv[2]
    location = []
    command1 = "set vlans VLAN%s vlan-id %s" % (vlan, vlan)
    command2 = "set interfaces %s.0 family ethernet-swithcing vlan members VLAN%s" % (interface, vlan)
    location.append(command1)
    location.append(command2)

    print location

#    send_config = conn.load_configuration(action='set',config='set system location country-code SE')
#    print send_config.tostring

#    check_config = conn.validate()
#    print check_config.tostring

#    compare_config = conn.compare_configuration()
#   print compare_config.tostring

#    conn.commit()
    conn.unlock()
    conn.close_session()

if __name__ == '__main__':
 connect('192.168.142.99', 'juniper', 'juniper')
