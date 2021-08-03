names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy", "Joy", "Katie", "Maddie", "Trash", "Nic", "Rachael", "Bec", "Bec", "Tabitha", "Teagan", "Viv", "Anna", "Catherine", "Catherine"
"Debby", "Gab", "Megan", "Michelle", "Nic", "Roxy", "Samara", "Sasha", "Sophie", "Teagan", "Viv"]

names_count = {}

for name in names:
    if name in names_count:
        names_count[name] += 1
    else:
        names_count[name] = 1

# Add items to the dictionery
# Create a dictionery with no contents
# Use a For loop to go through the list to perform a count
# Count is done using a if and else statement
# EG. if the value exists in the dictionery then add one 
# Else the value equals 1, the loop will start at Maddy and add 1 value
# then continue to Bel = 1, then Elnaz = 1, then Gia = 1, Izzy = 1, Joy = 1, Katie = 1
# Maddie = 1, Trash = 1, Nic = 1, Rachael = 1, Bec = 1
# however Bec occurs again and the loop is told to add 1 to the name so Bec value now = 2
# this is how the loops works until it gets the end of the list = names
# print(names_count) # we can now print the dictionary to see its new contents
# ie {'Maddy': 1, 'Bel': 1, 'Elnaz': 1, 'Gia': 1, 'Izzy': 1, 'Joy': 1, 'Kate': 1, 'Maddie': 1, 'Trash': 1, 'Nic': 1, 'Racheal': 1, 'Bec': 2 etc .....}
#Now the dictionery has contents we need to print this dictionary in the format required 
#Perform another loop for the dictionery using the key and value 
#Also using the function.items
#Request to print this loop 
for name, count in names_count.items():
    print(f"{name}: {count}")