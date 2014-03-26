data = open('nycdonors-cleanme.csv', 'r').readlines()[1:]

output = []

for line in data:
    line = line.replace('\r\n', '')
    line = line.split(',')

    line[11] = line[11].upper()
    line[15] = line[15].replace('&nbsp;', ' ')
    line[17] = str(line[17])
    line[20] = float(line[20])

    output.append(line)

print output