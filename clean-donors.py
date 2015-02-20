# This variable represents the data from the nycdonors-cleanme.csv file as a
# list, with each item representing a string for each row. 
data = open('nycdonors-cleanme.csv', 'r').read().split('\r\n')[1:]

# You'll add your output data here, using the .append() method
output = []

# Hint: Start by looping over the data variable, turn each item into a list,
# and perform the necessary transformations. Once the row has been transformed,
# append it into the output list, like this: output.append(cleaned_row)

########## YOUR CODE GOES HERE ##########