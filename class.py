# list=['kamal', 'ahmad', 'uzair']
# print(list[::2])
# print(list[-3::2])

# # append (add an element at the end of the list)
# list.append('ali')
# print(list)

# print(list.count('ahmad')) # count the number of occurrences of an element in the list


# make a list of 4 subjects tke user input add all subject marks  using userinput amd print sub marks with subject names
# subjects = []
# for i in range(4):
#     sub_name = input(f'Enter the name of subject {i+1}: ')
#     sub_marks = int(input(f'Enter the marks for {sub_name}: '))
#     subjects.append((sub_name, sub_marks))

# for sub_name, sub_marks in subjects:
#     print(f'{sub_name}: {sub_marks}')  

# Lab task: Create a list of 4 subjects, take user input for each subject's name and marks, and then print the subject names along with their corresponding marks.
# subjects = []
# sub1_name = input('Enter the name of subject 1: ')
# sub1_marks = int(input(f'Enter the marks for {sub1_name}: '))
# subjects.append((sub1_name, sub1_marks))

# sub2_name = input('Enter the name of subject 2: ')
# sub2_marks = int(input(f'Enter the marks for {sub2_name}: '))
# subjects.append((sub2_name, sub2_marks))

# sub3_name = input('Enter the name of subject 3: ')
# sub3_marks = int(input(f'Enter the marks for {sub3_name}: '))
# subjects.append((sub3_name, sub3_marks))

# sub4_name = input('Enter the name of subject 4: ')
# sub4_marks = int(input(f'Enter the marks for {sub4_name}: '))
# subjects.append((sub4_name, sub4_marks))


# # for sub_name, sub_marks in subjects:
# #     print(f'{sub_name}: {sub_marks}') 

# # output will be without for loop
# # print(f'{sub1_name}: {sub1_marks}')
# # print(f'{sub2_name}: {sub2_marks}')
# # print(f'{sub3_name}: {sub3_marks}')
# # print(f'{sub4_name}: {sub4_marks}')

# print(subjects)  # print the list of subjects and marks
# # use the subject list where we append subject names and marks and print the output without using for loop
# print(f'{subjects[0][0]}: {subjects[0][1]}')
# print(f'{subjects[1][0]}: {subjects[1][1]}')
# print(f'{subjects[2][0]}: {subjects[2][1]}')
# print(f'{subjects[3][0]}: {subjects[3][1]}')


# tuple (immutable list) in which we can not change the values of tuple once it is created

# dictonary (key-value pair) in which we can store data in key-value format key is unique and value can be anything (string, int, list, tuple, etc.)  key will not be repeated but value can be repeated  and keys can be of any data type (string, int, float, etc.) and values can be of any data type (string, int, float, list, tuple, etc.)  and we can access the value using the key and we can also update the value using the key and we can also delete the key-value pair using the key and we can also get all the keys and values using the keys() and values() methods respectively
# key can not be changed once it is created but value can be changed and we can also add new key-value pair using the key and value and we can also delete the key-value pair using the key and we can also get all the keys and values using the keys() and values() methods respectively
# sub={
#     'name': 'hamza',
#     'age': 20,
#     'city': 'Karachi'
# }
# print(sub['name'])  # access the value using the key
# # delete age
# del sub['age']
# print(sub)  # print the dictionary after deleting the key-value pair



# create calculator and operator will be in tuple and use lists and ditionary and if else statement to perform the operation and print the result
# operators = ('+', '-', '*', '/')
# list= []
# a = int(input('Enter first number: '))
# list.append(a)
# b = int(input('Enter second number: '))
# list.append(b)
# operator = input('Enter operator: ')
# if operator in operators:
#     if operator == '+':
#         result = list[0] + list[1]
#     elif operator == '-':
#         result = list[0] - list[1]
#     elif operator == '*':
#         result = list[0] * list[1]
#     elif operator == '/':
#         result = list[0] / list[1]
#     print(f'Result: {result}')
# else:
#     print('Invalid operator')



















import re
from unittest import result


oper=('+','-','*','/')
lis=[]
s=int(input('Enter first number: '))
lis.append(s)
t=int(input('Enter second number: '))
lis.append(t)
oper=input('Enter operator: ')
 
if oper=='+':
    result=lis[0]+lis[1]
elif oper=='-':
    result=lis[0]-lis[1]
elif oper=='*':
    result=lis[0]*lis[1]
elif oper=='/':
    result=lis[0]/lis[1]


print(f'the result came from : {lis[0]} {oper} {lis[1]} =', result)
# print(f'Result: {result}')