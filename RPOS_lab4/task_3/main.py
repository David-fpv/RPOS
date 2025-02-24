def get_int_vlan_map (file_name):
    access_dictionary = dict()
    trunk_dictionary = dict()
    with open(file_name) as file:
        blocks = file.read().split('!')

        for block in blocks:
            words = block.split()

            if len(words) <= 5:
                continue

            if words[0] != 'interface':
                continue
            
            if words[4] == "access":
                if len(words) <= 7:
                    access_dictionary[words[1]] = 1
                else:
                    access_dictionary[words[1]] = int(words[8])

            if words[3] == "trunk":
                vlan_list = list()
                for vlan in words[10].split(','):
                    vlan_list.append(int(vlan))
                trunk_dictionary[words[1]] = vlan_list

    return (access_dictionary, trunk_dictionary)
        



access_dictionary, trunk_dictionary = get_int_vlan_map("config_sw2.txt")

print("Access:")
print(access_dictionary)
print()
print("Trunk")
print(trunk_dictionary)
