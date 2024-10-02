#string: string is a data type that store the sequence of character
# string can be denoted by 1. "" 2. '' 3. ''' ''' 
# (reason: to use  a single quote, double quote in statement and to avoid the confusion we had these quote to denote the string)
# if we have to write few lines in a python we can't be able to write it with new lines or with tab :-
#thatswhy we use escape sequence character in a python:-\n,\t

#  example:-

# str="this is a string we are creating to display the character,\n To show how the sequence of characters stores in a string, \n and use of escape character"
# print(str)

# OPERATIONS IN A STRING:1. CONCATENATION:- "HELLO"+"WORLD"----> we use concatenation to add to character

# str1="bhumika"
# str2="motwani"
# final_str="str1+str2"
# print("concatention of the strings:",final_str)

                        #2. LENGHT OF STRing :- Len(str)------>we use this function to find the lenght of the string we have putinto it
# str1="bhumika"
# print(len(str1))

# str2="motwani"
# print(len(str2))

# final_str=str1+str2
# print(final_str)
# print(len(final_str))
 
#INDEXING:-B H U M I K A  _   M O T  W  A  N  I [WHEN WE USE STRING,STRING GIVES EACH CHARACTER INDEX]
        #  0 1 2 3 4 5 6  7   8 9 10 11 12 13 14[ str[]]

# str="bhumikamotwani"
# print(str[2])

#SLICING OF STRING:- acessing the part of string......>#syntax:- str[startind_idx : ending_idx]
                    ##NEGATIVE SLICING......># syntax:- str[-startind_idx : -ending_idx] A  P  P  L  E
                                                                                     #  -5 -4 -3 -2 -1

# str=[1:4]      is "hum" it does not take the 4th idx             

# str="bhumikamotwani"
# print(str[1:4])#hum
# print(str[:7])#bhumika
# print(str[0:])#bhumikamotwani
# print(str[0: len(str)])#bhumikamotwani
# print(str[-7:-1])#MOTWAN.....>negative slicing

# STRINGS FUNCTIONS:- 
# str="bhumikamotwani"
# 1.str.endswith("ani").....>return true if string ends with substr
# 2.str.capitalize().....>capitalize the 1st char
# 3.str.replace(old,new).....>replaces all occurence with new 
# 4.str.find(word).....>return 1st index with 1st occurrer
# 5.str.count(motwa)..>counts the occurence of substr(kitni bar exist karta hai uska count)
# substr means part of string use in a function

# str="i am studing from bhumika motwani\n i study pathon from bhumika"
# print(str.endswith("mika"))
# print(str.capitalize())
# print(str.replace("bhumika","prashu"))
# print(str.find("study"))
# print(str.count("bhumika")) 

#write a program to input users first name and print its lenght??

# name=input("enter your name:")
# lenght=len(name)
# print("hello"+ name + "!your name has " +str(lenght)+ "character.")# by just a + sign we print our value in " double quotes we use use print statement"

#wap to find the occurrence of '$' in a string

# str="the currency of america is $"
# print(str.find("$"))
