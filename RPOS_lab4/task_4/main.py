ignore_list = ['duplex', 'alias', 'Current configuration']

def ignore_command (command, ignore):
    ignore_command = False

    for word in ignore:
        if word in command:
            return True
    return ignore_command


def config_to_dict (filename):
    config_dictionary= dict()
    with open(filename) as file:
        lines_with_blanks = file.read().split('\n')
        lines = list()
        for line in lines_with_blanks:
            if len(line) > 1:
                lines.append(line)

        for line_number in range(len(lines)):

            if lines[line_number][0] == '!' or ignore_command(lines[line_number], ignore_list):
                continue

            if lines[line_number][0] != ' ':
                subcommands = list()

                i = 1
                while(True):
                    if line_number + i < len(lines) and lines[line_number + i][0] == ' ':
                        if not ignore_command(lines[line_number + i], ignore_list):
                            subcommands.append(lines[line_number + i][1:])
                        i += 1
                    else:
                        break

                config_dictionary[lines[line_number]] = subcommands

    return config_dictionary


output_dictionary = config_to_dict('config_sw1.txt')
for i in output_dictionary:
    print(i)
    print(output_dictionary[i])
    print()