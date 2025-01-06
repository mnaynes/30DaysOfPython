import json
import os
file_path = 'C:/Users/Michael Naynes/Documents/Programming/Python/30DaysOfPython/day_19'
countries_data_file = os.path.join(file_path, 'countries_data.json')

def most_populated_countries(filename, rank_count):
    file = open(filename, encoding='utf8') # set encoding due to encoding error when reading file
    countries_data = json.load(file) # return file as a dictionary
    file.close()

    country_population = get_countries_population(countries_data)
    # country_population = sorted(country_population, key=lambda x:(x['population']))
    # print(country_population)

    top_ranked_values = list(set(map(lambda dict: dict['population'], country_population)))
    print(top_ranked_values)
    top_ranked_values.sort(reverse=True)
    print(top_ranked_values)

    
    ranked_list = []
    for value in top_ranked_values:
        ranked_list += list(filter(lambda dict: dict['population'] == value, country_population))
        if len(ranked_list) >= rank_count: break
    
    return ranked_list

def get_countries_population(data):
    return [ {'country': item['name'], 'population': item['population']} for item in data ]

# print(most_populated_countries(countries_data_file, 10))
print(most_populated_countries(countries_data_file, 3))