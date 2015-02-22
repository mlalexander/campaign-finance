# This variable represents the data from the nycdonors-cleanme.csv file as a
# list, with each item representing a string for each row.
data = open('nycdonors-cleanme.csv', 'r').read().split('\r\n')[1:]

# You'll add your output data here, using the .append() method
output = []

# Hint: Start by looping over the data variable, turn each item into a list,
# and perform the necessary transformations. Once the row has been transformed,
# append it into the output list, like this: output.append(cleaned_row)

########## YOUR CODE GOES HERE ##########

for row in data:
    row_list = row.split(",")
    row_list[11] = row_list[11].upper()
    row_list[15] = row_list[15].replace("&NBSP;", " ")
    row_list[20] = float(row_list[20])
    row_list[17] = str(row_list[17])

    if row_list[20] > 5000:
        print row_list

    if row_list[16] != "NY":
        print row_list

    output.append(row_list)

print output
