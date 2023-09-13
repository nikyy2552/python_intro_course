value_1 = int(input('Please enter first value!'))
value_2 = int(input('Please enter second value!'))

if value_1 > value_2:
    value_2 = value_1
    print(value_2)

elif value_2 > value_1:
    value_1 = value_2
    print(value_1)

else:
    print('The two values are equal!')
    print(value_1, value_2)
