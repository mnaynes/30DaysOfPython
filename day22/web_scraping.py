import requests
from bs4 import BeautifulSoup
import json

# url = 'https://archive.ics.uci.edu/dataset/320/student+performance'

# Lets use the requests get method to fetch the data from url

# response = requests.get(url)

# content = response.content # we get all the content from the website
# soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
# print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
# print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # gives the whole page on the website
# print(response.status_code)

# tables = soup.find_all('flex-container')
# # We are targeting the table with cellpadding attribute with the value of 3
# # We can select using id, class or HTML tag , for more information check the beautifulsoup doc
# table = tables[0] # the result is a list, we are taking out data from it
# for td in table.find('tr').find_all('td'):
#     print(td.text)


############################################################################

def concat_value_strings(tag, attr=None):
    value = ''

    value_tags = tag.find_all(attrs={'class' : attr}) if attr is not None else tag.children
    for value_tag in value_tags:
        value += value_tag.string
    
    return value

def keys_exist(data, key1, key2):
    if key1 in data:
        if key2 in data[key1]:
            return True

    return False

url = 'https://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

json_data = []
data = {}
category = ''
fact = ''
for tag in soup.find('article').descendants:
    if 'class' in str(tag) and tag.has_attr('class'):

        if 'stat-group-title' in tag['class']:
            category = tag.string.strip()
            data[category] = {}
        
        elif 'bu-stat-title' in tag['class'] or 'stat-label' in tag['class']:
            fact = tag.string.strip()
            if category in data:
                data[category].update({fact : ''})
        
        elif 'bu-stat-value-container' in tag['class']:
            value = concat_value_strings(tag, 'bu-stat-value-field')
            
            if keys_exist(data, category, fact):
                data[category][fact] = value
        
        elif 'stat-figure' in tag['class']:
            value = concat_value_strings(tag)
            
            if keys_exist(data, category, fact):
                data[category][fact] = value

json_data.append(data)

print(json.dumps(json_data))

# facts_dictionary = {}
# values_dictionary = {}

# def record_count(dictionary, key):
#     if key in dictionary:
#         dictionary[key] += 1
#     else:
#         dictionary[key] = 1

# def get_child_tags(html, parent_attr, child_attr, dictionary):
#     if parent_attr in dictionary:
#         return html.find_all(attrs={'class':parent_attr})[dictionary[parent_attr]]\
#                 .find_all(attrs={'class':child_attr})
#     else:
#         return html.find(attrs={'class':parent_attr}).find_all(attrs={'class':child_attr})

# def get_facts(html, parent_attr, child_attr):
#     facts = get_child_tags(html, parent_attr, child_attr, facts_dictionary)
    
#     record_count(facts_dictionary, parent_attr)
    
#     return [ fact.string.strip() for fact in facts ]

# def get_values(html, parent_attr, child_attr1, child_attr2=None):
#     value_tags = get_child_tags(html, parent_attr, child_attr1, values_dictionary)

#     values = []
#     for tags in value_tags:
#         # print(f'==={tags}')
#         # print(tags.find_all(attrs={'class' : child_attr2}))

#         tags = tags.find_all(attrs={'class' : child_attr2}) if child_attr2 is not None else tags.children
#         complete_string = ''
#         for value in tags:
#             complete_string += value.string
#         values.append(complete_string)

#     record_count(values_dictionary, parent_attr)

#     return values

# category_tags = soup.find_all(attrs={'class' : 'stat-group-title'})
# categories = [category.string.strip() for category in category_tags]

# for category in categories:
#     if category == 'Quick Facts & Stats':
#         category_attr = 'bu-stat-list'
#         fact_attr = 'bu-stat-title'
#         value_attr = 'bu-stat-value-container'
#         sub_value_attr = 'bu-stat-value-field'
#     elif category == 'Community':
#         category_attr = 'stat-section'
#         fact_attr = 'stat-label'
#         value_attr = 'stat-figure'
#         sub_value_attr = None
#     elif category == 'Campus':
#         category_attr = 'bu-stat-list'
#         fact_attr = 'bu-stat-title'
#         value_attr = 'bu-stat-value-container'
#         sub_value_attr = 'bu-stat-value-field'
#     elif category == 'Academics':
#         category_attr = 'stat-section'
#         fact_attr = 'stat-label'
#         value_attr = 'stat-figure'
#         sub_value_attr = None

#     facts = get_facts(soup, category_attr, fact_attr)
#     values = get_values(soup, category_attr, value_attr, sub_value_attr)
#     facts_values = dict(zip(facts, values))
#     json_data.append({category : facts_values})

############################################################################

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

############################################################################

def get_column_names(table):
    col_names = []
    for tag in table.find('tr').find_all('th'):
        col_names.append(join_data_strings(tag.children, ' '))
    
    return col_names

def exclude_none_tags(tags):
    return [ BeautifulSoup(str(tag), 'html.parser') for tag in tags \
            if not str(tag).isspace() and not tag.string ]

def join_data_strings(tags, delimiter=''):
    data = [ tag.string for tag in tags if tag.string ]
    return delimiter.join(data).strip()

def has_span_with_date_class(tag):
    if 'date' in str(tag) \
        and tag.span.has_attr('class') \
        and 'date' in tag.span['class']:
        return True
    
    return False

def cleanup_data(data):
    return [ item.replace('\xa0', ' ') for item in data \
                if not item.isspace() and item != '']

def create_data_list(tags, delimiter=''):
    data = []
    for tag in tags:
        if tag.string:
            data.append(tag.string)
        else:
            data.append(join_data_strings(tag.children, delimiter))
            
    return cleanup_data(data)


url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

json_data = []
table = soup.find(attrs={'class':'wikitable'})
columns = get_column_names(table)
for tr in exclude_none_tags(table.tr.next_siblings):

    row_data = []
    column_index = 0
    for td in exclude_none_tags(tr.tr.children):
        if column_index == 0:
            row_data.append(td.a.string)
        elif column_index == 1:
            row_data.append(td.img['src'])
        elif column_index == 2 \
            or column_index == 3:
            if has_span_with_date_class(td):
                row_data.append(join_data_strings(td.td.span.children, ' '))
            else:
                row_data.append(join_data_strings(td.td.children, ' '))
        elif column_index == 4 \
            or column_index == 5:
            row_data.append(create_data_list(td.td.children))
        elif column_index == 6:
            row_data.append(create_data_list(td.td.children, ' '))
        
        column_index += 1
    
    json_data.append(dict(zip(columns,row_data)))

print(json.dumps(json_data))