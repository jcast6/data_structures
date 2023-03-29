dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print ("\ndict['Name']: ", dict['Name'])
print ("\ndict['Age']: ", dict['Age'])

print(type(dict))

x = dict.keys()
print("\ndict keys" , x)

# get name attribute in dict
print("\nLooking for name: ", dict['Name'])

# change dict key value:
dict['Age'] = 8

# new value in 'Age' key
print(dict)

# check if key exists
if 'Name' in dict:
    print("\nName is a key in the dictionary")

else:
    print("\nKey is not in dictionary")


# add Key to dictionary:
dict['Address'] = "123 Ave"

print("\nThe new dict", dict)

# get list of values
y = dict.values()
print("\n", y)

# remove individual Keys from dictionary
del dict['Age']
print("Delete age Key, new dict", dict)

# clear the all elements in the dictionary
dict.clear()
print("dictionary is clear", dict)

# delete the dictionary
del dict
print("deleted dictionary")




