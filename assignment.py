
print('===== Python Calculator =====')
print('Author: Hamza')
print('Version: 1.0')

oper = {
    1: 'addition',
    2: 'subtraction',
    3: 'multiplication',
    4: 'division'
}

selection = int(input('Enter your selection: '))
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

if selection == 1:
    result = num1 + num2
elif selection == 2:
    result = num1 - num2
elif selection == 3:
    result = num1 * num2
elif selection == 4:
    result = num1 / num2
else:
    print('Invalid selection')
    exit()

print('Operation:', oper[selection])
print('Result:', result)

