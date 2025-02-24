def print_information (ospf_route):
    column_names = ["Protocol", "Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]

    ospf_route = ospf_route.replace(',', '')
    ospf_route = ospf_route.replace('via', '')
    words = ospf_route.split()
    words[0] = 'OSPF'

    answer = dict(zip(column_names, words))

    for key, value in answer.items():
        print("%-20s %-12s" % (key + ":", value))


file = open('./ospf.txt', 'r')
data = file.read()
lines = data.split('\n')

for line in lines:
    print_information(line)
    print()

