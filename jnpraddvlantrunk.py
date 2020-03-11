#!/usr/bin/env python

import sys

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
    command2 = "set interfaces %s.0 family ethernet-switching vlan members VLAN%s" % (interface, vlan)
    command3 = "set interfaces %s.0 family ethernet-switching interface-mode trunk" % (interface)
    location.append(command1)
    location.append(command2)
    location.append(command3)

    send_config = conn.load_configuration(action='set',config=location)

    conn.commit()
    conn.unlock()
    conn.close_session()

if __name__ == '__main__':
 connect('192.168.120.3', 'juniper', 'juniper')
