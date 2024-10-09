import random as rand
import string
import sys

ALPHANUMERIC = string.ascii_letters + string.digits
MAX_RGB = 256
MIN_RGB = 0

# rand.choices() can return duplicate elements
# rand.sample() returns unique elements unless sequence has duplicates
def random_user_id(char_len):
    id = str()
    for iter in range(char_len):
        id += rand.choice(ALPHANUMERIC)

    return id

def user_id_gen_by_user():
    char_len = int(input('Enter number of characters: '))
    id_count = int(input('Enter number of IDs: '))

    ids = []
    for iter in range(id_count):
        ids.append(random_user_id(char_len))
    
    return ids

def rgb_color_gen():
    # return [rand.randrange(MAX_RGB), rand.randrange(MAX_RGB), rand.randrange(MAX_RGB)]
    return 'rgb({}, {}, {})'.format(rand.randrange(MAX_RGB), rand.randrange(MAX_RGB), rand.randrange(MAX_RGB))
    # return rand.randint(MIN_RGB, MAX_RGB)

def random_hexa():
    len_of_hex = 6
    hexa = str()
    for iter in range(len_of_hex):
        hexa += rand.choice(string.hexdigits)
    return f'#{hexa}'

def list_of_hexa_colors(hexa_count=1):
    hexas = []
    for iter in range(hexa_count):
        hexas.append(random_hexa())
    
    return hexas

def list_of_rgb_colors(rgb_count=1):
    rgbs = []
    for iter in range(rgb_count):
        rgbs.append(rgb_color_gen())
    
    return rgbs

def generate_colors(color_format, color_count=1):
    if color_format.lower() == 'hexa':
        return list_of_hexa_colors(color_count)
    elif color_format.lower() == 'rgb':
        return list_of_rgb_colors(color_count)
    else:
        return 'hexa or rgb color formats only'

def shuffle_list(to_shuffle_list):
    rand.shuffle(to_shuffle_list)
    return to_shuffle_list

def gen_7_numbers():
    return rand.sample(string.digits, k=7)

print(random_user_id(5))
print(user_id_gen_by_user())
print(rgb_color_gen())
print(list_of_hexa_colors())
print(list_of_rgb_colors(3))
print(generate_colors('RGB'))

test = ['Python', 'Numpy','Pandas','Django', 'Flask']
# print(shuffle_list(test))

print(gen_7_numbers())
