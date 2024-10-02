# LIST IN PYTHON:-a list is a built-in data type used to store collections of items or elements.WHhich can store diff type of elements(int,float,str)and it allows the codes to be modify anytime.
#strings=immutable,but the lists are mutable(which can be changed)               


# student_marks=["muskan",'bangalore',10.3,50.5,60.8,56.6]
# print(student_marks)
# print(type(student_marks))
# print(len(student_marks))
# print(student_marks[2])
# print(student_marks[3])

#LIST_SLICING:-
# List slicing in Python is a technique that allows you to access specific portions or "slices" of a list

# #BASIC SLICING
# my_list = [10, 20, 30, 40, 50, 60]
# slice_1 = my_list[1:4]  # Returns elements from index 1 to 3
# print(slice_1)  # Output: [20, 30, 40]

# # Omitting Start or Stop: You can omit the start or stop to slice from the beginning or until the end.

# slice_2 = my_list[:3]   # Starts from index 0 (default) to index 2
# print(slice_2)  # Output: [10, 20, 30]

# slice_3 = my_list[2:]   # Starts from index 2 to the end
# print(slice_3)  # Output: [30, 40, 50, 60]

# # Using Negative Indices:Negative indices allow you to slice from the end of the list.

# slice_4 = my_list[-4:-1]  # Returns elements from index -4 to -2
# print(slice_4)  # Output: [30, 40, 50]

# # Slicing with a Step:You can specify a step to control the spacing between elements.

# slice_5 = my_list[::2]   # Returns every second element
# print(slice_5)  # Output: [10, 30, 50]

# # Reversing a List with Slicing:Using a negative step, you can reverse a list.

# reversed_list = my_list[::-1]  # Reverses the list
# print(reversed_list)  # Output: [60, 50, 40, 30, 20, 10]


# LIST METHOD:-These methods provide essential functionalities for managing and manipulating lists in Python.


# append(value)

# Adds value to the end of the list.BUT IT ADDS ONLY ONE VALUE
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]


# extend()
# Adds elements from iterable (IT EXTEND THE LIST BY USING MORE THAN 1 VALUE) to the end of the list.
# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# print(my_list)  # Output: [1, 2, 3, 4, 5]



# insert(index, value)
# Inserts value at the specified index.
# my_list = [1, 2, 3]
# my_list.insert(1, 'a')  # Insert 'a' at index 1
# print(my_list)  # Output: [1, 'a', 2, 3]


# remove(value)
# Removes the first occurrence of value from the list.
# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list)  # Output: [1, 3, 2]


# pop(index)
# Removes and returns the element at index (last element if no index specified).
# my_list = [1, 2, 3]
# my_list.pop()  #it revomes the last value
# print(my_list)  # Output: [1, 2]


# clear()
# Removes all elements from the list.
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)  # Output: []


# index(value)
# Returns the index of the first occurrence of value.it replaces the value we want 
# my_list = [1, 2, 3]
# my_list.index(2)
# print(my_list.index(2))  # Output: 1


# count(value)
# Returns the number of occurrences of value in the list.
# my_list = [1, 2, 3, 2]
# my_list.count(2)
# print(my_list.count(2))  # Output: 2


# sort()
# 1.Sorts the elements of the list in ascending order.
# Example: my_list.sort().
# 2.Sorts the elements of the list in Descending order.
#Example: my_list.sort(reverse=true).

# reverse()
# Reverses the order of the elements in the list.
# list=[1,2,3,4]
# list.reverse()
# print(list)



# TUPLES:- A built-in data type used to store AND LET US CREATE.IMMUTABLE SEQUEMCE OF VALUE.
# TUPLES ARE PURELY SIMILAR TO THE LISTS BUT THE ONLY DIFFERENCE IS THAT TUPLES IS IMMUTABLE WHICH CANNOT ALLOW USER TO 
# TO CHANGE THE VALUE MIDDLE OF THE CODE IT CANNOT ASSIGN VALUES AS WE DO IN LISTS

# WE CAN DIFFER THE TUPLES FROM LIST BY USINGS () LIKEWISE LIST USES [].

TUPLE=(1,2,3,4)
print(TUPLE.index(2))