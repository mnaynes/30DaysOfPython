import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
splitted = re.findall(r'\w+', paragraph)
unique_words = list(set(splitted))
count = list(map(splitted.count, unique_words))
word_freq = [ (count, word) for word, count in zip(unique_words, count) ]
word_freq.sort(reverse=True)
print(word_freq)

task_2 = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
points = re.findall(r'-?\d+', task_2)
points = list(map(int, points))
points.sort()
distance = points[len(points)-1] - points[0]
print(distance)

def is_valid_variable(var):
    match = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var)
    if match:
        print(f'{var} is a valid variable name.')
    else:
        print(f'{var} is not a valid variable name.')

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)
print(cleaned_sentence)

def most_frequent_words(text):
    splitted = text.split()
    unique_words = list(set(splitted))
    count = list(map(splitted.count, unique_words))
    word_freq = [ (count, word) for word, count in zip(unique_words, count) ]
    word_freq.sort(reverse=True)

    return word_freq

print(most_frequent_words(cleaned_sentence))