from functools import reduce

'''
map() applies a function to each item in a lsit
filter() returns a list of items that returned True when used in the function
reduce() returns a value that was cummulated results from applying a function to each item in a list 
all functions above has takes 2 parameters: a function and a list
'''

'''
higher order function takes one or more functions as parameters and can return results from another function 
closure is a nested function in a function that can access elements from the outer function
decorators a design patter to add a new function in an existing function without modifying that existing function
'''

strs = [' me maybe', ' me later', ' me never']

def call(phrase):
    return 'This is call' + phrase

def call_filter(phrase):
    # print(phrase)
    if phrase.endswith('er'):
        return True
    return False

def call_reduce(p1, p2):
    return p1 + p2

phrases = map(call, strs)
list_of_phrases = list(phrases)
print(list_of_phrases)
# print(list(phrases)) # result from list(phrases) will only return the list once. if called again, it will return empty
                        # calling phrases will return the function object. this is same with filter()


filtered_phrases = filter(call_filter, list_of_phrases)
print(list(filtered_phrases))

concat_phrases = reduce(call_reduce, strs)
print(concat_phrases)   # reduce()'s output does not behave the same with map() and filter()

#######################################################

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for country in countries:
#     print(country)

# for name in names:
#     print(name)

# for number in numbers:
#     print(number)

########################################################

def to_upper(string):
    return string.upper()

country_upper = map(to_upper, countries)
# country_upper = map(lambda string: string.upper(), countries)
print(list(country_upper))

########################################################

def square(number):
    return number ** 2

number_squared = map(square, numbers)
print(list(number_squared))

########################################################

name_upper = map(to_upper, names)
print(list(name_upper))

########################################################

country_land2 = filter(lambda country: 'land' in country, countries)
print(list(country_land2))

country_six = filter(lambda country: len(country) == 6, countries)
print(list(country_six))

country_six_more = filter(lambda country: len(country) >= 6, countries)
print(list(country_six_more))

country_starts_e = filter(lambda country: country.lower().startswith('e'), countries)
print(list(country_starts_e))

# skipping #8
# test = map(to_upper, countries).filter(lambda country: 'land' in country, countries).reduce(lambda acc, curr: acc + curr, countries)

def get_string_lists(item):
    return str(item)

string_nums = map(get_string_lists, numbers)
print(list(string_nums))

########################################################

sum_nums = reduce(lambda acc, curr: acc+curr, numbers)
print(sum_nums)

########################################################

def concat_countries(acc, curr):
    return f'{acc}, {curr}'
concat_countries = reduce(concat_countries, countries)

concat_countries = reduce(lambda acc, curr: f'{acc}, {curr}', countries)
end_concatenator = ', and'
concat_countries = concat_countries[::-1].replace(',', end_concatenator[::-1], 1)[::-1]
print('{} are north European countries'.format(concat_countries))

# ########################################################

from countries import *

def categorize_countries(countries):
    def category(substr):
        filtered = filter(lambda country: country.endswith(substr), countries)
        return list(filtered)
    return category

categorize_by = categorize_countries(countries)
print(categorize_by('land'))
print(categorize_by('island'))
print(categorize_by('ia'))
print(categorize_by('stan'))

########################################################

def count_countries(countries):
    def count_country_by(key):
        return len(list(filter(lambda country: country.lower().startswith(key.lower()), countries)))
    
    return count_country_by

count_countries_by = count_countries(countries)
initials = set(map(lambda k: k[0], countries))
counts = list(map(lambda initial: count_countries_by(initial), initials))
country_dict = dict(map(lambda initial,count : (initial,count), initials, counts))
print(country_dict)

########################################################

def get_countries(type):
    if type == 'get_first_ten_countries':
        return get_first_ten_countries
    elif type == 'get_last_ten_countries':
        return get_last_ten_countries
    
def get_first_ten_countries(countries):
    return countries[:10]

def get_last_ten_countries(countries):
    return countries[:-11:-1]

result = get_countries('get_first_ten_countries')
print(result(countries))
result = get_countries('get_last_ten_countries')
print(result(countries))

########################################################

import json
from collections import OrderedDict

file = open('C:/Users/Michael Naynes/Documents/Programming/Python/30DaysOfPython/day_14/countries-data.py', encoding='utf8') # set encoding due to encoding error when reading file
countries_data = json.load(file) # return file as a dictionary
file.close()

def sort_countries(type):
    if type == 'sort_by_name_capital_popu':
        return sort_by_name_capital_popu

def sort_by_name_capital_popu(country_data):
    return sorted(country_data, key=lambda x:(x['name'], x['capital'], x['population']))

def sort_by_key(country_data):
    def sort_by(key):
        return sorted(country_data, key=lambda x:(x[key]))
    
    return sort_by

sort_ = sort_countries('sort_by_name_capital_popu')
sorted_name_capital_popu = sort_(countries_data)

sort_countries_by = sort_by_key(countries_data)
sorted_by_name = sort_countries_by('name')
sorted_by_capital = sort_countries_by('capital')
sorted_by_population = sort_countries_by('population')


def rank_country_attr(countries_data):
    def top_most(rank_count, country_attr):
        get_attr = get_countries_attr(country_attr)
        attr_stats, sort_key = get_attr(countries_data)

        attr_stats = sorted(attr_stats, key=lambda x:(x[sort_key]), reverse=True)
        top_ranked_values = list(set(map(lambda dict: dict[sort_key], attr_stats)))
        top_ranked_values.sort(reverse=True)

        ranked_list = []
        for value in top_ranked_values:
            ranked_list += list(filter(lambda dict: dict[sort_key] == value, attr_stats))
            if len(ranked_list) >= rank_count: break
        
        return ranked_list
    
    return top_most

def get_countries_attr(type):
    if type == 'languages':
        return get_countries_languages_count
    elif type == 'population':
        return get_countries_population

# def sort_by_value(dictionary):
#     return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

def get_languages(data):
    return data['languages']

def get_countries_languages_count(data):
    countries_languages = [ language for country in list(map(get_languages, data)) for language in country ]
    languages = set(countries_languages)
    language_count = list(map(countries_languages.count, languages))

    return [ {'language': language, 'count': lang_count} for language, lang_count in zip(languages, language_count) ], 'count'

def get_countries_population(data):
    return [ {'name': item['name'], 'population': item['population']} for item in data ], 'population'

rank_by = rank_country_attr(countries_data)
ten_most_spoken_language = rank_by(10, 'languages')
print(ten_most_spoken_language)
ten_most_populated = rank_by(10, 'population')
print(ten_most_populated)


