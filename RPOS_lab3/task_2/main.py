import sys

if len(sys.argv) != 3:
    print('Error. You need to specify 2 parameters.')
    exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

output_lines = []

with open(input_file_name) as file_input:
    ignore = ['duplex', 'alias', 'Current configuration', 'ip']
    file_data = file_input.read()
    file_lines = file_data.split('\n')

    for line in file_lines:
        flag = 1
        
        for ignore_word in ignore:
            if ignore_word in line:
                flag = 0
                break

        if flag == 1:
            output_lines.append(line)
            if line[0] != '!':
                print(line)


for i in range(len(output_lines)):
    if i + 1 < len(output_lines):
        output_lines[i] += '\n'

with open(output_file_name, 'w') as file_output:
    file_output.writelines(output_lines)