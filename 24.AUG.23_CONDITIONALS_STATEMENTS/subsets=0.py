print('Welcome!\n This program will show you if your subset of three numbers have a result equal to 0')
number_1 = int(input('Please enter first number! '))
number_2 = int(input('Please enter second number! '))
number_3 = int(input('Please enter third number! '))

if number_1 + number_2 and number_1 + number_3 and number_2 + number_3 == 0:
    print('A subset is equal to zero! ')
    print(number_1 + number_2, number_1 + number_3, number_2 + number_3)

else:
    print('No subset equal to zero! ')

