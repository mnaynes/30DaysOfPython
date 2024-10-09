for iter in range(11):
    print(iter)

iter = 0
while iter < 11:
    print(iter)
    iter += 1

########################################################

for iter in range(10,-1,-1):
    print(iter)

iter = 10
while iter > 0:
    print(iter)
    iter -= 1

########################################################

for iter in range(7):
    for iter2 in range(iter+1):
        print('#', end='')
    print()

########################################################

for iter in range(8):
    for iter2 in range(8):
        print('# ', end='')
    print()

########################################################

for iter in range(11):
    print(f'{iter} x {iter} = {iter**2}')

########################################################

for item in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(item)

########################################################

for iter in range(101):
    if iter % 2 == 0:
        print(iter, end = ' ')
print()

########################################################

for iter in range(101):
    if iter % 2 != 0:
        print(iter, end = ' ')
print()

########################################################

sum = 0
for iter in range(101):
    sum += iter
print('The sum of all numbers is {}.'.format(sum))

########################################################

sum_even = 0
sum_odd = 0
for iter in range(101):
    if iter % 2 == 0:
        sum_even += iter
    else:
        sum_odd += iter
print('The sum of all evens is {}. And the sum of all odds is {}.'.format(sum_even, sum_odd))

########################################################

from countries import countries

for country in countries:
    if 'land' in country:
        print(country)

########################################################

fruits = ['banana', 'orange', 'mango', 'lemon']
for iter in range(len(fruits)-1, -1, -1):
    print(fruits[iter])

########################################################

import json

file = open('countries-data.py', encoding='utf8') # set encoding due to encoding error when reading file
countries_data = json.load(file) # return file as a dictionary
file.close()

country_languages = set()
for country in countries_data:
    country_languages.update(country['languages'])
print('What are the total number of languages in the data: {}'.format(len(country_languages)))

language_count_dict = {}
for country in countries_data:
    for langs in country['languages']:
        if language_count_dict.get(langs) == None:
            language_count_dict[langs] = 1
        else:
            language_count_dict[langs] += 1
sorted_language_count_dict = {k: v for k, v in sorted(language_count_dict.items(), key=lambda item: item[1], reverse=True)} # sort dictionary by values
print('Find the ten most spoken languages from the data:')
for iter, country in zip(range(10), sorted_language_count_dict):
    print('{}. {} - {} countries'.format(iter+1, country, sorted_language_count_dict[country]))

population_count_dict = {}
for country in countries_data:
    population_count_dict[country['name']] = country['population']
sorted_population_count_dict = {k: v for k, v in sorted(population_count_dict.items(), key=lambda item: item[1], reverse=True)} # sort dictionary by values
print('Find the 10 most populated countries in the world:')
for iter, country in zip(range(10), sorted_population_count_dict):
    print('{}. {} - {}'.format(iter+1, country, sorted_population_count_dict[country]))
