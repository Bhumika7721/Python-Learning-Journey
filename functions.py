# FUNCTION IN PYTHON:-
# BLOCK OF STATEMENT THAT PERFORM A SPECIFIC TASK.basically it reduces the problam of redundant (repeatation)

# Syntax:-def func_nam(param1,param2)#some work ......>function definition(it tell us what function can do)
    # input=parameter #output=returns
             # return value....>returns the value to the function
        #  func_name(arg1,arg2)# function call

#simple programe for sum of two number using functions

#function definition
# def calc_sum(a,b):#parametrs
#     return a+b


#function call
# sum1=int(input("enter the value of a: "))
# sum2=int(input("enter the value of b :"))
# result=calc_sum(sum1,sum2)#sum1=a sum2=b...we have to store the function in something(jese yaha result me kia )
# print("the sum of two number:-",result)


#function call
# sum=calc_sum(55,88)#55=a 88=b
# print(sum)

# write a programe to find average of 4 numbers

# def avg_num(num1, num2, num3, num4):
#     return (num1 + num2 + num3 + num4) / 4

# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))
# num3 = int(input("Enter the number 3: "))
# num4 = int(input("Enter the number 4: "))

# average = avg_num(num1, num2, num3, num4)
# print("The average of the 4 numbers is:", average)

# function has 2 type built in and user define function 

#builtin function
# 1.print()
# 2.len()
# 3.type()
# 4.range()

#userdefine

# keywords in python:

# import keyword
# print(keyword.kwlist)

#swapinng of number using function(with return with argument)
 
# def sum(a,b):
#     a,b=b,a 
#     return(a,b) 
# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# print(sum(a,b))


# no argument no return:-input output operation perform in def section.only calling outter function.
#no return with argument:-if we can pass the argument in a def section input outof- function.output and operation inside of function.
#return but no argument:-output is perf outside the function other details inside the functon
#return with argument:-input and output outside of function and operation inside the function...