# # while True:
# #     print('Hamza')

# # print('this is multiplication', 3*4)

# # print(12,12, sep='-')



# print('loading...')
# print('A', 'B', 'C', sep='')
# # print('line1\nline2')
# print('line1\nline2', sep='')
# # print('line1')
# # print('line2')

# print('kamal', 'my name is: ')

# print('dark web" is the engine"')   #dark web is in single quote and engine is in double quote








# Calculator
# print('                                  This is my first lab')
# print('                                  Author:Hamza')
# print('                                  version 1.0')

# a= int(input('Enter first number: '))
# selection = input('Enter your selection: ')
# b= int(input('Enter second number: '))

# # method 1
# if selection == '+':
#     result = a + b
# elif selection == '-':
#     result = a - b
# elif selection == '*':
#     result = a * b
# elif selection == '/':
#     result = a / b

# print('The output is: ',result)

# # method 2

# print('The sum of two numbers is: ', a+b)
# print('The difference of two numbers is: ', a-b)
# print('The product of two numbers is: ', a*b)







print('                                  This is my first lab')
print('                                  Author:Hamza')
print('                                  version 1.0')

selection = input('Enter your selection (+, -, *, /): ')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

op= {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a / b
}

print('The output is:', op[selection])