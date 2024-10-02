age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need {} more year/s to learn to drive.'.format(18-age))

########################################################

your_age = input('Enter your age: ')
my_age = 29
age_diff = int(your_age) - my_age
if age_diff == 0:
    print('We are the same age.')
else:
    year_form = 'year'
    if abs(age_diff) > 1:
        year_form = 'years'

    age_comparison = 'younger'
    if age_diff > 0:
        age_comparison = 'older'

    print('You are {} {} {} than me'.format(abs(age_diff), year_form, age_comparison))

########################################################

a = input('Enter number one: ')
b = input('Enter number two: ')
if a > b:
    print('{} is greater than {}'.format(a, b))
elif a < b:
    print('{} is smaller than {}'.format(a, b))
else:
    print('{} is equal to {}'.format(a, b))

########################################################

score = input('Enter score: ')
try:
    score = int(score)
except ValueError:
    print("That's not an int!")
    exit()

if score < 0 or score > 100:
    print('Invalid score input.')
else:
    if score >= 80:
        rating = 'A'
    elif score >= 70 and score <= 79:
        rating = 'B'
    elif score >= 60 and score <= 69:
        rating = 'C'
    elif score >= 50 and score <= 59:
        rating = 'D'
    elif score <= 49:
        rating = 'F'

    print('Your rating is {}'.format(rating))

########################################################

autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

month = input('Enter month: ')
month = month.lower()

if month in autumn:
    season = 'Autumn'
elif month in winter:
    season = 'Winter'
elif month in spring:
    season = 'Spring'
elif month in summer:
    season = 'Summer'

try:
    print('The month is in {} season.'.format(season))
except NameError:
    print('Invalid input')

########################################################

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruit = input('Enter a fruit: ')
if fruit not in fruits:
    fruits.append(fruit)
else:
    print('That fruit already exist in the list')
print(fruits)

########################################################

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person.get('skills') != None:
    print('Skill in the middle of the list: ' + 
          person['skills'][len(person.get('skills'))//2])
    
    if 'Python' in person['skills']:
        print('Person has Python skill')

    frontend_skills = ['Javascript', 'React']
    backend_skills = {'Node', 'Python', 'MongoDB'}
    fullstack_skills = {'React', 'Node', 'MongoDB'}

    if frontend_skills == person['skills']: print('He is a front end developer')
    elif fullstack_skills.issubset(person['skills']): print('He is a fullstack developer')
    elif backend_skills.issubset(person['skills']): print('He is a backend developer')
    else: print('unknown title')

if person['first_name'] and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married.'.format(person['first_name'],
                                                     person['last_name'],
                                                     person['country']))