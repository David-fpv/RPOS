def is_line_with_MAC (line):
    words = line.split()

    for word in words:
        flag = 1
        octets = word.split('.')
        if len(octets) != 3:
            continue
        else:
            for octet in octets:
                if len(octet) != 4:
                    flag = 0
                    break

                try:
                    value = int(octet, 16)
                except ValueError:
                    flag = 0
                    break
                
                if value < 0 and value > 65535:
                    flag = 0
                    break
            if flag == 1:
                return True
    return False


def take_first_element (line):
    try:
        return int(line.split()[0])
    except ValueError:
        print('Incorrect file format. Please review the correctness of the entered vlan number.')
        exit()


with open('CAM_table.txt') as file:  

    lines = file.readlines()
    lines_with_MAC = []

    for line in lines:
        line = line.replace('\n', '')
        if is_line_with_MAC(line):
            lines_with_MAC.append(line)

    lines_with_MAC = sorted(lines_with_MAC, key=take_first_element)
    
    vlan_numbers = input('Please, input vlans numbers ')   

    for line in lines_with_MAC:
        vlan = line.split()[0]
        if vlan in vlan_numbers:
            print(line)

    

