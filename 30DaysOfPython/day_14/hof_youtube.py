'''
higher order functions from youtube
a function that either:
1. accepts a function as an argument
or
2. returns a function
(In python, functions are also treated as objects)
'''

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func, phrase='Hello'):
    text = func(phrase)
    print(text)

phrase = 'hehe'
hello(loud, phrase)
hello(quiet)

###############################################################

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

# x will be set to 2 and it will stay that way until we finish this program
# divide now contains the function object dividend
divide = divisor(2)
print(divide(10))