import math

age = int()
height = float()
complex_number = complex()

b = input('Enter base: ')
h = input('Enter height: ')
area_of_triangle = 0.5*float(b)*float(h), 2
print('The area of the triangle is', area_of_triangle)

a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
perim_of_triangle = float(a) + float(b) + float(c), 2
print('The perimeter of the triangle is', perim_of_triangle)

l = input('Enter length: ')
w = input('Enter width: ')
area_of_rectangle = float(l)*float(w)
print('The area of the rectangle is', area_of_rectangle)
perim_of_rectangle = 2*(float(l)+float(w))
print('The perimeter of the rectangle is', perim_of_rectangle)

r = input('Enter radius: ')
area_of_circle = math.pi * (float(r)**2)
print('The area of the circle is', round(area_of_circle, 2))
circum_of_circle = 2 * math.pi * float(r)
print('The circumference of the circle is', round(circum_of_circle, 2))

equation = 'y = 2x - 2'
print('Equation:', equation)
print('x-intercept: x = 1')
print('y-intercept: y = -2')
print('P1 = (1, 0)')
x1 = 1
y1 = 0
print('P2 = (0, -2)')
x2 = 0
y2 = -2
slope1 = (y2-y1)/(x2-x1)
print('The slope of', equation, 'is', slope1)

p1 = '(2, 2)'
print('P1 =', p1)
x1 = 2
y1 = 2
p2 = '(6, 10)'
print('P2 =', p2)
x2 = 6
y2 = 10
slope2 = (y2-y1)/(x2-x1)
print('The slope of', p1, 'and', p2, 'is', slope2)
euclidean_distance = math.sqrt(((x1-x2)**2) + ((x2-y2)**2))
print('The Euclidean distance of', p1, 'and', p2, 'is', round(euclidean_distance, 2))

if slope1 == slope2:
    print("Both slopes are equal.")
else:
    print("Both slopes are not equal")

equation2 = 'y = x^2 + 6x + 9'
print('Equation:', equation2)
a = 1
b = 6
c = 9
x_positive = (-b + math.sqrt((b**2)-(4*a*c))) / (2*a)
x_negative = (-b - math.sqrt((b**2)-(4*a*c))) / (2*a)

if x_positive == x_negative:
    print('Using the quadratic formula, x is equal to', x_positive)
else:
    print('Using the quadratic formula, x is equal to', x_positive, 'and', x_negative)

string1 = 'python'
string2 = 'dragon'
print(string1, 'is', len(string1), 'characters')
print(string2, 'is', len(string2), 'characters')
if len(string1) == len(string2):
    print(string1, 'is not the same length as', string2)

sentence = 'I hope this course is not full of jargon.'
if 'jargon' in sentence:
    print('\'jargon\' is in the sentence, \'' + sentence + '\'')

if 'on' in string1:
    print('There is no \'on\' in', string1)
if 'on' in string2:
    print('There is no \'on\' in', string2)

print('float type:', float(len(string1)))
print('string type:', str(len(string1)))

num = input('Enter integer: ')
if int(num) % 2 == 0:
    print(num, 'is an even number')
else:
    print(num, 'is an odd number')

if 7 // 3 == int(2.7):
    print('7 // 3 = int(2.7)')
else:
    print('7 // 3 != int(2.7)')

if type('10') == type(10):
    print('type(\'10\') == type(10)')
else:
    print('type(\'10\') != type(10)')

# '9.8' cannot be converted directly to int, convert to float first
if int(float('9.8')) == 10:
    print('int(\'9.8\') == 10')
else:
    print('int(\'9.8\') != 10')

hours = input('Enter hours: ')
rate_per_hour = input('Enter rate per hour: ')
earning = int(rate_per_hour) * int(hours)
print('Your weekly earning is', earning)

years = input('Enter number of years you have lived: ')
seconds = int(years) * 365 * 24 * 60 * 60
print('You have lived for', seconds, 'seconds')

print('''1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125''')

max_base = 5
max_exponent = 4
i = 1
while i <= max_base:
    j = 0
    print(i, end=" ")
    while j < max_exponent:
        print(i**j, end=" ")
        j+=1
    i+=1
    print()