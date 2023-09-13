
total_academic_time = int(input('Please enter course time in academic hours and press enter! '))

course_time_in_astro_hours = total_academic_time * 45
academic_time_in_minutes = total_academic_time * 45
brake = 15 * total_academic_time
total_astronomical_time = (academic_time_in_minutes + brake)

print('Total course time will be:', course_time_in_astro_hours / 60, 'Astronomical hours without brakes')
print('Or', total_astronomical_time / 60, 'Astronomical hours with 15 minutes brake for every single hour')
