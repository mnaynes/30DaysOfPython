# Source: https://www.geeksforgeeks.org/measuring-the-document-similarity-in-python/

import math 
import os
import string 
import sys 
  
# reading the text file 
# This function will return a  
# list of the lines of text  
# in the file. 
def read_file(filename):  
      
    try: 
        with open(filename, 'r') as f: 
            data = f.read() 
        return data 
      
    except IOError: 
        print("Error opening or reading input file: ", filename) 
        sys.exit() 
  
# splitting the text lines into words 
# translation table is a global variable 
# mapping upper case to lower case and 
# punctuation to spaces 
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase, 
                                     " "*len(string.punctuation)+string.ascii_lowercase)

print(f'translation_table: {translation_table}')
       
# returns a list of the words 
# in the file 
def get_words_from_line_list(text):  
      
    text = text.translate(translation_table) 
    print(f'get_words_from_line_list()\ntext: {text}')
    word_list = text.split()
    print(f'get_words_from_line_list()\nword_list: {word_list}')
      
    return word_list 
  
  
# counts frequency of each word 
# returns a dictionary which maps 
# the words to  their frequency. 
def count_frequency(word_list):  
      
    D = {} 
      
    for new_word in word_list: 
          
        if new_word in D: 
            D[new_word] = D[new_word] + 1
              
        else: 
            D[new_word] = 1
              
    return D 
  
# returns dictionary of (word, frequency) 
# pairs from the previous dictionary. 
def word_frequencies_for_file(filename):  
    # print(f'word_frequencies_for_file()\nfilename: {filename}')
    line_list = read_file(filename) 
    word_list = get_words_from_line_list(line_list) 
    freq_mapping = count_frequency(word_list) 
  
    print("File", filename, ":", ) 
    print(len(line_list), "lines, ", ) 
    print(len(word_list), "words, ", ) 
    print(len(freq_mapping), "distinct words") 
  
    return freq_mapping 
  
  
# returns the dot product of two documents 
def dotProduct(D1, D2):  
    Sum = 0.0
      
    for key in D1: 
          
        if key in D2: 
            Sum += (D1[key] * D2[key]) 
              
    return Sum
  
# returns the angle in radians  
# between document vectors 
def vector_angle(D1, D2):  
    numerator = dotProduct(D1, D2) 
    denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2)) 
      
    return math.acos(numerator / denominator) 
  
  
def documentSimilarity(filename_1, filename_2): 
      
    # filename_1 = sys.argv[1] 
    # filename_2 = sys.argv[2] 
    sorted_word_list_1 = word_frequencies_for_file(filename_1) 
    sorted_word_list_2 = word_frequencies_for_file(filename_2) 
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2) 
    
    # Where 0 degree means the two documents are exactly identical and
    # 90 degrees indicate that the two documents are very different.
    print("The distance between the documents is: % 0.6f (radians)"% distance)

file_path = 'C:/Users/Michael Naynes/Documents/Programming/Python/30DaysOfPython/day_19'
speeches = ['obama_speech.txt', 'michelle_obama_speech.txt', 'donald_speech.txt', 'melina_trump_speech.txt']

obama = os.path.join(file_path, speeches[0])
donald = os.path.join(file_path, speeches[2])
# Driver code 
documentSimilarity(obama, donald) 