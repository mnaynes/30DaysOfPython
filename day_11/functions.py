import math

def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(2,4))

########################################################

def area_of_circle(r):
    return round(math.pi * r**2,4)

print(area_of_circle(13))

########################################################

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) != int:
            return 'Contains invalid input'
        sum += num
    return sum

print(add_all_nums(5,6,8,4,6,9,2,4))

########################################################

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(convert_celsius_to_fahrenheit(32))

########################################################

autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

def check_season(month):
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
        return '{} is in {} season.'.format(month.capitalize(), season)
    except NameError:
        return 'Invalid input'
    
print(check_season('January'))

########################################################

def calculate_slope(x_int, y_int):
    return (y_int - 0) / (0 - x_int)

print(calculate_slope(1, -1))

########################################################

def solve_quadratic_eqn(a, b, c):
    x_positive = (-b + math.sqrt((b**2)-(4*a*c))) / (2*a)
    x_negative = (-b - math.sqrt((b**2)-(4*a*c))) / (2*a)

    if x_positive == x_negative:
        return 'Using the quadratic formula, x = {}'.format(x_positive)
    
    return 'Using the quadratic formula, x = {} or x = {}'.format(x_positive, x_negative)

print(solve_quadratic_eqn(1,6,9))

########################################################

def print_list(L):
    for item in L:
        print(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
print_list(fruits)

########################################################

def reverse_list(reverse_L):
    # print(reverse_L[::-1])
    L = []
    for iter in range(len(reverse_L)-1,-1,-1):
        L.append(reverse_L[iter])
    return L

print(reverse_list(fruits))

########################################################

def capitalize_list_items(items):
    cap_list = []
    for iter in range(len(items)):
        cap_list.append(items[iter].capitalize())
    
    return cap_list

print(capitalize_list_items(fruits))

########################################################

def add_item(items, new_item):
    new_list = []
    new_list = items.copy()
    new_list.append(new_item)
    return new_list

print(add_item(fruits, 'grape'))

########################################################

def remove_item(items, del_item):
    new_list = []
    new_list = items.copy()
    new_list.remove(del_item)
    return new_list

print(remove_item(fruits, 'orange'))

########################################################

def sum_of_numbers(num):
    sum = 0
    for n in range(1,num+1):
        sum += n
    return sum

print(sum_of_numbers(100))

########################################################

def sum_of_odds(num):
    sum = 0
    for n in range(1,num+1,2):
        sum += n
    return sum

print(sum_of_odds(7))

########################################################

def sum_of_even(num):
    sum = 0
    for n in range(2,num+1,2):
        sum += n
    return sum

print(sum_of_even(6))

########################################################

def evens_and_odds(num):
    num_of_odds = 0
    num_of_evens = 0

    for n in range(num+1):
        if n % 2 == 0:
            num_of_evens += 1
        else:
            num_of_odds += 1
    
    print('Then number of odds are {}.'.format(num_of_odds))
    print('Then number of evens are {}.'.format(num_of_evens))

evens_and_odds(100)

########################################################

def factorial(whole_num):
    fact = 1
    for n in range(1,whole_num+1):
        fact *= n
    
    return fact

print(factorial(6))

########################################################

def is_empty(param):
    if len(param) == 0:
        return 'Array is empty.'
    else:
        return 'Array is not empty.'

print(is_empty([]))

########################################################

test = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def calculate_mean(nums):
    return sum(nums)/len(nums)

def calculate_median(nums):
    sorted_nums = nums.copy()
    sorted_nums.sort()
    if len(sorted_nums) % 2 == 0:
        median = (sorted_nums[int(len(sorted_nums)/2)] + sorted_nums[int(len(sorted_nums)/2-1)]) / 2 # follows PEMDAS
    else:
        median = sorted_nums[int(len(sorted_nums)//2)] / 2
    
    return median

def calculate_mode(nums):
    mode_dict = {}
    for num in nums:
        if mode_dict.get(num) == None:
            mode_dict[num] = 1
        else:
            mode_dict[num] += 1
    
    sorted_mode_dict = {k: v for k, v in sorted(mode_dict.items(), key=lambda item: item[1], reverse=True)} # sort dictionary by values

    for num in sorted_mode_dict:
        return num

def calculate_range(nums):
    sorted_nums = nums.copy()
    sorted_nums.sort()
    return sorted_nums[-1] - sorted_nums[0]

def calculate_variance(nums):
    mean = calculate_mean(nums)

    sum_nom = 0
    for num in nums:
        sum_nom += (num - mean) ** 2
    
    return sum_nom / (len(nums) - 1)

def calculate_std(nums):
    return math.sqrt(calculate_variance(nums))

print(calculate_mean(test))
print(calculate_median(test))
print(calculate_mode(test))
print(calculate_range(test))
print(calculate_variance(test))
print(calculate_std(test))

########################################################

def is_prime(num):
    if(num > 1):
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i == 0):
                return False
        return True
    else:
        return False

print(is_prime(6))

########################################################

test = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
test2 = [19, 22, 20, 26, 25, 24]

def are_unique_items(items):
    new_set = set(items)
    if len(new_set) == len(items):
        return True
    
    return False

print(are_unique_items(test2))

########################################################

test = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
test2 = [19, 22, 19, 'asdf', 20, 25, [], 24, 25, 24]

def contains_one_data_type(items):
    the_type = ''
    for item in items:
        if the_type == '':
            the_type = type(item)
        else:
            if the_type != type(item):
                return False
    
    return True

print(contains_one_data_type(test2))

########################################################

import re

def is_valid_var(var_name):
    if re.findall(r"^[_A-Za-z]\w*$", var_name):
        return True
    return False

print(is_valid_var('#ahahaJFD'))

########################################################

import json

def most_spoken_languages(countries_data, rank_count):
    language_count_dict = {}
    for country in countries_data:
        for langs in country['languages']:
            if language_count_dict.get(langs) == None:
                language_count_dict[langs] = 1
            else:
                language_count_dict[langs] += 1
    sorted_language_count_dict = {k: v for k, v in sorted(language_count_dict.items(), key=lambda item: item[1], reverse=True)} # sort dictionary by values

    for iter, country in zip(range(rank_count), sorted_language_count_dict):
        print('{}. {} - {} countries'.format(iter+1, country, sorted_language_count_dict[country]))

def most_populated_countries(countries_data, rank_count):
    population_count_dict = {}
    for country in countries_data:
        population_count_dict[country['name']] = country['population']
    sorted_population_count_dict = {k: v for k, v in sorted(population_count_dict.items(), key=lambda item: item[1], reverse=True)} # sort dictionary by values

    for iter, country in zip(range(rank_count), sorted_population_count_dict):
        print('{}. {} - {}'.format(iter+1, country, sorted_population_count_dict[country]))

file = open('countries-data.py', encoding='utf8') # set encoding due to encoding error when reading file
countries_data = json.load(file) # return file as a dictionary
file.close()

most_spoken_languages(countries_data,10)
most_populated_countries(countries_data,10)