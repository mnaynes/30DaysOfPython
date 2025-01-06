import json

def read_file_dictionary(filename):
    file = open(filename, encoding='utf8') # set encoding due to encoding error when reading file
    data = json.load(file) # return file as a dictionary
    file.close()

    return data

def get_country_and_property(data, property):
    return [ {'country': item['name'], property: item[property]} for item in data ]

def get_unique_properties_in_reverse_order(data_dict, property):
    unique_props = list(set(map(lambda dict: dict[property], data_dict)))
    return sorted(unique_props, reverse=True)

def get_top_ranked_values(data_dict, property, top_ranked_values, rank_count):
    ranked_list = []
    for value in top_ranked_values:
        ranked_list += list(filter(lambda dict: dict[property] == value, data_dict))
        if len(ranked_list) >= rank_count: break
    
    return ranked_list

