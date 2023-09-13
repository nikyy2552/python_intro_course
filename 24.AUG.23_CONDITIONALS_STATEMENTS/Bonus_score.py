scores = int(input('Please enter scores between 1 and 9 '))


if scores == 1 or scores == 2 or scores == 3:
    scores *= 10
    print('Your score multiplier is 10!', 'Your final scores is:', scores, '!')
elif scores == 4 or scores == 5 or scores == 6:
    scores *= 100
    print('Your scores are multiplier is 100!', 'Your final scores is:', scores, '!')
elif scores == 7 or scores == 8 or scores == 9:
    scores *= 1000
    print('Your score multiplier is 1000!', 'Your final scores is:', scores, '!')
else:
    print('Wrong scores! ')
