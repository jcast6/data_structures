list1= ['math', 'soccer', 'swimming', 200, 300]
list2= [1, 2, 3, 4, 5, 6]
list3= ["a", "b", "c", "d"]

print("list1", list1)
#printing the first element '0' in list1
print ("list1[0]: ", list1[0])

#printing the second through fifth elements of list2
print("\nlist2[1:5]: ", list2[1:5])

#updating list
list1[2]= 'physics'
print("\nlist1[2]", list1[2])

#print the list3
print("\nlist3:", list3)

#delete element from list3
del list3[3]
print("\nlist3 after deletion", list3)

"""
BASIC LIST OPERATIONS

Python Expression	             Results	                Description
len([1, 2, 3])	                   3	                        Length

[1, 2, 3] + [4, 5, 6]	      [1, 2, 3, 4, 5, 6]	        Concatenation

['Hi!'] * 4	[              'Hi!', 'Hi!', 'Hi!', 'Hi!']	     Repetition

3 in [1, 2, 3]	                 True	                    Membership

for x in [1, 2, 3]:                                         Iteration
    print x,	1 2 3	                

"""