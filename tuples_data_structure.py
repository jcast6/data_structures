tuple1 = ('soccer', 'hockey', 'baseball', 123)
tuple2 = (45, 658, 453, 3, 1)
tuple3 = ("b", "z", "n", "q")

# printing tuple elements
print("tupple1[0]: ", tuple1[0])
print("tuple2[1:5]: ", tuple2[1:5])


# tuples are immutable(cannot change elements values) but you can merge tuples together
tuple4 = tuple1 + tuple3

print(tuple4)


# delete tuple
del tuple1
print(tuple1) # error due to deletion 



'''
expression                 results                          description
len((1, 2, 3))	              3	                                 Length
(1, 2, 3) + (4, 5, 6)       (1, 2, 3, 4, 5, 6)	                Concatenation
('Hi!',) * 4	            ('Hi!', 'Hi!', 'Hi!', 'Hi!')	     Repetition
3 in (1, 2, 3)	                True	                          Membership
for x in (1, 2, 3): print x,	1 2 3	                         Iteration
'''