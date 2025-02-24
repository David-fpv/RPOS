access_list_input = {'FastEthernet0/12':10,
                     'FastEthernet0/14':11,
                     'FastEthernet0/16':17,
                     'FastEthernet0/17':150
                     }

access_comands = ['interface ',
                  'switchport mode access',
                  'switchport access vlan ',
                  'switchport nonegotiate',
                  'spanning-tree portfast',
                  'spanning-tree bpduguard enable',
                  ]

port_security = ['switchport port-security maximum 2',
                 'switchport port-security violation restrict',
                 'switchport port-security'
                 ]


def access_ports_generate (access_list, psecurity=False):
    access_dictionary_output = dict()
    
    for port, vlan in access_list.items():
        access_list_output = []
        access_list_output.append(access_comands[0] + port)
        access_list_output.append(access_comands[1])
        access_list_output.append(access_comands[2] + str(vlan))
        access_list_output.append(access_comands[3])
        access_list_output.append(access_comands[4])
        access_list_output.append(access_comands[5])

        if psecurity == True:
            for command in port_security:
                access_list_output.append(command)

        access_dictionary_output[port] = access_list_output

    return access_dictionary_output

for port, commands in access_ports_generate(access_list_input, True).items():
    print(port)
    for command in commands:
        print(command)
    print()

