# import webbrowser # web browser module to open websites

# # list of urls: python
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# # opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

######################################################################################################

# import requests # importing the request module

# url = 'https://www.w3.org/TR/controller-document/#controllers' # text from a website

# response = requests.get(url) # opening a network and fetching a data
# # print(response)
# # print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# # print(response.text) # gives all the text from the page

######################################################################################################

# import requests
# url = 'https://restcountries.com/v3.1/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[1:2])  # we sliced only the first country, remove the slicing to see all countries

######################################################################################################

import os, re

def get_top_ranked_values_nondict(data, top_ranked_values, rank_count):
    ranked_list = []
    for value in top_ranked_values:
        ranked_list += list(filter(lambda dict: dict[0] == value, data))
        if len(ranked_list) >= rank_count: break
    
    return ranked_list

file_path = 'C:/Users/Michael Naynes/Documents/Programming/Python/30-Days-Of-Python-master/data'
rnj_txt = os.path.join(file_path, 'romeo_and_juliet.txt')

rnj_file = open(rnj_txt)
romeo_and_juliet = rnj_file.read()
rnj_file.close()

words = re.findall(r'\w+', romeo_and_juliet.lower())

unique_words = set(words)

count = list(map(words.count, unique_words))

word_freq = [ (count, word) for word, count in zip(unique_words, count) ]

top_ranked_values = sorted(list(set(count)), reverse=True)
print(get_top_ranked_values_nondict(word_freq, top_ranked_values, 10))

# ######################################################################################################

import requests
from statistics import mean, median, stdev
from pandas import DataFrame, read_json

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)  # opening a network and fetching a data
cats = response.json()

def convert_range_to_ints(range):
    numbers = re.findall(r'\d+', range)
    return [int(number) for number in numbers]

def compress_list(lists):
    return [ item
                for list in lists
                    for item in list ]

def print_statistics(data, label):
    print(f'Minimum {label}: {min(data)}')
    print(f'Maximum {label}: {max(data)}')
    print(f'Mean {label}: {mean(data)}')
    print(f'Median {label}: {median(data)}')
    print(f'Standard Deviation {label}: {stdev(data)}')

cat_weights = [ convert_range_to_ints(cat['weight']['metric'])
                    for cat in cats ]
weights = compress_list(cat_weights)
print_statistics(weights, 'weight')

cat_lifespans = [ convert_range_to_ints(cat['life_span'])
                        for cat in cats ]
lifespans = compress_list(cat_lifespans)
print_statistics(lifespans, 'life span')

cat_countries = [ cat['origin'] for cat in cats ]
countries = list(set(cat_countries))
countries_freq = list(map(cat_countries.count, countries))

data = {
    "Country" : countries,
    "No. of Cat Breeds" : countries_freq,
}

df = DataFrame(data)
print(df)

# def get_min_weight(weights):
#     return min(get_weights(weights))

# def get_max_weight(weights):
#     return max(get_weights(weights))

# def get_mean_weight(weights):
#     return mean(get_weights(weights))

# def get_median_weight(weights):
#     return median(get_weights(weights))

# def get_stdv_weight(weights):
#     return stdev(get_weights(weights))


# cat_min_weight = [{'breed' : cat['name'], 'min_weight' : get_min_weight(cat['weight']['metric'])}
#                     for cat in cats]
# print(cat_min_weight)
# cat_max_weight = [{'breed' : cat['name'], 'max_weight' : get_max_weight(cat['weight']['metric'])}
#                     for cat in cats]
# print(cat_max_weight)
# cat_mean_weight = [{'breed' : cat['name'], 'mean_weight' : get_mean_weight(cat['weight']['metric'])}
#                     for cat in cats]
# print(cat_mean_weight)
# cat_median_weight = [{'breed' : cat['name'], 'median_weight' : get_median_weight(cat['weight']['metric'])}
#                     for cat in cats]
# print(cat_median_weight)
# cat_stdv_weight = [{'breed' : cat['name'], 'stdv_weight' : get_stdv_weight(cat['weight']['metric'])}
#                     for cat in cats]
# print(cat_stdv_weight)

######################################################################################################

url = 'https://restcountries.com/v3.1/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
countries = response.json()

raw_df = DataFrame.from_dict(countries)

def get_country_and_property(data, property):
    return [ {'country': item['name']['official'], property: item[property]} for item in data ]

def get_unique_values_in_reverse_order(data_dict, property):
    unique_props = list(set(map(lambda dict: dict[property], data_dict)))
    return sorted(unique_props, reverse=True)

def get_top_ranked_values(data_dict, property, rank_count):
    ranked_list = []

    top_ranked_values = get_unique_values_in_reverse_order(data_dict, property)

    for value in top_ranked_values:
        ranked_list += list(filter(lambda dict: dict[property] == value, data_dict))
        if len(ranked_list) >= rank_count: break
    
    return ranked_list

country_area = get_country_and_property(countries, 'area')
largest_countries = get_top_ranked_values(country_area, 'area', 10)
largest_countries_df = DataFrame.from_dict(largest_countries)
largest_countries_df.columns = largest_countries_df.columns.str.title()
print('\nThe 10 largest countries\n', largest_countries_df)


languages_df = raw_df['languages'].dropna()
languages_data = [ language for languages in languages_df
                                for language in languages.values()]

languages = set(languages_data)
language_count = []
for language in languages:
    language_count.append({'language' : language, 'count' : languages_data.count(language)})

most_spoken_languages = get_top_ranked_values(language_count, 'count', 10)
most_spoken_languages_df = DataFrame.from_dict(most_spoken_languages)
most_spoken_languages_df.columns = most_spoken_languages_df.columns.str.title()
print('\nThe 10 most spoken languages\n', most_spoken_languages_df)


print(f'\nTotal number of languages in the world: {len(languages)}')

######################################################################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://archive.ics.uci.edu/dataset/53/iris'
html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

# for tag in soup.find_all(True):
#     print(tag.name)
