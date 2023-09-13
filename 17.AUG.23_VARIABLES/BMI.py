# THIS PROGRAM WILL OUTPUT BMI - BODY TO MAS RATIO BY GIVEN INPUT LIKE WEIGHT IN KILOGRAMS AND HEIGHT IN METERS

weight = float(input('Please enter your weight in kilograms and press Enter! '))
height = float(input('Please enter your height in meters and press Enter! '))

bmi = weight / (height * height)
print('Your body to mass ratio is: ', round(bmi))
