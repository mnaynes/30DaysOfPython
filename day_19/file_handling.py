import re
import os

def file_line_count(file):
    f = open(file)
    lines = f.readlines()
    return len(lines)

def file_word_count(file):
    f = open(file)
    words = re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", f.read())
    return len(words)

file_path = 'C:/Users/Michael Naynes/Documents/Programming/Python/30DaysOfPython/day_19'
speeches = ['obama_speech.txt', 'michelle_obama_speech.txt', 'donald_speech.txt', 'melina_trump_speech.txt']

# for speech in speeches:
#     print(speech)
#     file = os.path.join(file_path, speech)
#     print(f'Line Count: {file_line_count(file)}')
#     print(f'Word Count: {file_word_count(file)}')

import json

countries_data_file = os.path.join(file_path, 'countries_data.json')

def most_spoken_language(filename, rank_count):
    file = open(filename, encoding='utf8') # set encoding due to encoding error when reading file
    countries_data = json.load(file) # return file as a dictionary
    file.close()

    language_count = get_countries_languages_count(countries_data)
    language_count.sort(reverse=True)
    top_ranked_values = sorted(list(set(map(lambda lc: lc[0], language_count))), reverse=True)
    
    ranked_list = []
    for value in top_ranked_values:
        ranked_list += list(filter(lambda lc: lc[0] == value, language_count))
        if len(ranked_list) >= rank_count: break
    
    return ranked_list

def get_languages(data):
    return data['languages']

def get_countries_languages_count(data):
    countries_languages = [ language for country in list(map(get_languages, data)) for language in country ]
    languages = set(countries_languages)
    language_count = list(map(countries_languages.count, languages))

    return [ (lang_count, language) for language, lang_count in zip(languages, language_count) ]

# print(most_spoken_language(countries_data_file, 10))
# print(most_spoken_language(countries_data_file, 3))

def most_populated_countries(filename, rank_count):
    file = open(filename, encoding='utf8') # set encoding due to encoding error when reading file
    countries_data = json.load(file) # return file as a dictionary
    file.close()

    country_population = get_countries_population(countries_data)
    country_population = sorted(country_population, key=lambda x:(x['population']), reverse=True)

    top_ranked_values = list(set(map(lambda dict: dict['population'], country_population)))
    top_ranked_values.sort(reverse=True)
    
    ranked_list = []
    for value in top_ranked_values:
        ranked_list += list(filter(lambda dict: dict['population'] == value, country_population))
        if len(ranked_list) >= rank_count: break
    
    return ranked_list

def get_countries_population(data):
    return [ {'country': item['name'], 'population': item['population']} for item in data ]

# print(most_populated_countries(countries_data_file, 10))
# print(most_populated_countries(countries_data_file, 3))

data_path = 'C:/Users/Michael Naynes/Documents/Programming/Python/30-Days-Of-Python-master/data'
email_exchanges_big = 'email_exchanges_big.txt'

file = os.path.join(data_path, email_exchanges_big)
f = open(file)
incoming_email_adds = re.findall(r"From (:?[^\W_]+@[\w\d\.]+)", f.read())
# print(incoming_email_adds)

def find_most_frequent_words(filename, rank_count):
    word_count = get_words_count(filename)
    word_count.sort(reverse=True)
    top_ranked_values = sorted(list(set(map(lambda lc: lc[0], word_count))), reverse=True)
    
    ranked_list = []
    for value in top_ranked_values:
        ranked_list += list(filter(lambda lc: lc[0] == value, word_count))
        if len(ranked_list) >= rank_count: break
    
    return ranked_list

def get_words_count(data):
    f = open(data)
    words = clean_text(f.read())
    words = re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", words.lower())
    
    # use for loop instead to make the next 3 lines faster. this can iterate on the list of words once
    unique_words = set(words)
    word_count = list(map(words.count, unique_words))

    return [ (count, words) for words, count in zip(unique_words, word_count) ]

# for speech in speeches:
#     print(speech)
#     file = os.path.join(file_path, speech)
#     print(find_most_frequent_words(file, 10))
from stop_words import *

def clean_text(text):
    return re.sub(r'[^\w\s]', ' ', text)

def remove_support_words(text):
    text_words = re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", text.lower())
    # test = text.split()

    # filtered_words = []
    for stop_word in stop_words:
        # print(stop_word)
        text_words = [text_word for text_word in text_words if text_word != stop_word] 
    
    return ' '.join(text_words)

def check_text_similarity(text1: str, text2: str) -> str:
    if os.path.exists(text1):
        file = open(text1)
        text1 = file.read()
    
    if os.path.exists(text2):
        file = open(text2)
        text2 = file.read()
    
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    filtered_text1 = remove_support_words(text1)
    filtered_text2 = remove_support_words(text2)

    # print(filtered_text1)
    # print(filtered_text2)

# test = os.path.join(file_path, speeches[1])
# test2 = os.path.join(file_path, speeches[3])
# check_text_similarity(test, test2)


############################################################

romeo_and_juliet = 'romeo_and_juliet.txt'

def count_frequency(word_list):  
      
    D = {} 
      
    for new_word in word_list: 
          
        if new_word in D: 
            D[new_word] = D[new_word] + 1
              
        else: 
            D[new_word] = 1
              
    return D 

file_rnj = os.path.join(data_path, romeo_and_juliet)
# f = open(file_rnj)
# text_rnj = f.read()
# text_rnj = clean_text(text_rnj)
# words_rnj = re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", text_rnj.lower())

# freq = count_frequency(words_rnj)
# print(freq)

# print(find_most_frequent_words(file_rnj, 10))


############################################################

import csv

hacker_news = 'hacker_news.csv'
file_hn = os.path.join(data_path, hacker_news)

with open(file_hn) as f:
    csv_reader = csv.reader(f, delimiter=',')

    python_line_count = 0
    javascript_line_count = 0
    java_line_count = 0
    for row in csv_reader:
        line = ", ".join(row)

        if re.search('python', line, re.I):
            # print(f'python: {line}')
            python_line_count += 1

        if re.search('javascript', line, re.I):
            # print(f'js: {line}')
            javascript_line_count += 1
        
        # ref: https://stackoverflow.com/questions/977251/regular-expressions-and-negating-a-whole-character-group
        if re.search(r'java(?!script)', line, re.I):
            # print(f'java: {line}')
            java_line_count += 1
    
    print(f'Line count with \'Python\': {python_line_count}')
    print(f'Line count with \'Javascript\': {javascript_line_count}')
    print(f'Line count with \'Java\': {java_line_count}')

