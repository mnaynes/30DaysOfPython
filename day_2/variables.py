# Day 2: 30 Days of python programming

import math

first_name = 'Michael'
last_name = 'Naynes'
full_name = 'Michael Naynes'
country = 'Philippines'
city = 'Manila'
age = 29
year = 2024
is_married = False
is_true = True
is_light_on = True

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Michael', 'Naynes', 'Michael Naynes', 'Philippines', 'Manila', 29, 2024, False, True, True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))

if len(first_name) > len(last_name):
    print('first name is longer than last name')
elif len(first_name) < len(last_name):
    print('last name is longer than first name')
else:
    print('first name and last name are equal length')

num_one = 5
num_two = 4
print('num_one = 5, num_two = 4')
total = num_one + num_two
print('total =', total)
diff = num_two - num_one
print('diff =', diff)
product = num_two * num_one
print('product =', product)
division = num_one / num_two
print('division =', division)
remainder = num_two % num_one
print('remainder =', remainder)
exp = num_one ** num_two
print('exp =', exp)
floor_division = num_one // num_two
print('floor_division =', floor_division)

r = 30
print('r = ', r)
area_of_circle = math.pi * (r**2)
print('area_of_circle = ', area_of_circle)
circum_of_circle = 2 * math.pi * r
print('circum_of_circle = ', circum_of_circle)

r = input('Input radius: ')
r = int(r)
print('r = ', r)
area_of_circle = math.pi * (r**2)
print('area_of_circle = ', area_of_circle)
circum_of_circle = 2 * math.pi * r
print('circum_of_circle = ', circum_of_circle)

first_name = input('Input first_name: ')
last_name = input('Input last_name: ')
country = input('Input country: ')
age = input('Input age: ')

print('first_name:', first_name)
print('last_name:', last_name)
print('country:', country)
print('age:', age)

num = 123
print('haha',len(str(num)))