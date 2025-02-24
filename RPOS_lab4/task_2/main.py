trunk_template	= ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan ',
                  'switchport trunk allowed vlan ']

input_trunk_settings = {'FastEthernet0/1':[10,20],
                        'FastEthernet0/2':[11,30],
                        'FastEthernet0/4':[17]
                        }

def list_to_string_with_separator (input_list, separator_character):
    output_string = str()

    for i in range(len(input_list) - 1):
        output_string += str(input_list[i]) + separator_character
    output_string += str(input_list[len(input_list) - 1])

    return output_string

def trunk_generate_config (input_trunk_settings, trunk_template):
    trunk_output_dictionary = dict()

    for port, vlans in input_trunk_settings.items():
        for command in trunk_template:
            trunk_output_list_for_port = list()

            trunk_output_list_for_port.append(trunk_template[0])
            trunk_output_list_for_port.append(trunk_template[1])
            trunk_output_list_for_port.append(trunk_template[2] + str(vlans[0])) 

            vlan_string = list_to_string_with_separator(vlans, ',')
            trunk_output_list_for_port.append(trunk_template[3] + vlan_string)

            trunk_output_dictionary[port] = trunk_output_list_for_port

    return trunk_output_dictionary


for port, commands in trunk_generate_config(input_trunk_settings, trunk_template).items():
    print(port)
    for command in commands:
        print(command)
    print()
    
