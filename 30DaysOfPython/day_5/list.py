from countries import *

empty_list = []
print(empty_list)

rand_list = ['coffee', 'tea', 'matcha', 'frappe', 'mocha']

print(len(rand_list))

print('First item: {}\nMiddle item: {}\nLast item: {}'.format(rand_list[0], rand_list[len(rand_list)//2], rand_list[-1]))

mixed_data_types = ['Michael', 29, '163cm', 'Single', 'Tayabas']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_types)
print(it_companies)

print(len(it_companies))

print('First item: {}\nMiddle item: {}\nLast item: {}'.format(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1]))

it_companies[-1] = 'FactSet'
print(it_companies)

it_companies.append('Amazon')
print(it_companies)

it_companies.insert(len(it_companies)//2, 'Fujitsu')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print('#; '.join(it_companies))

print('IBM' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[3::])

print(it_companies[:len(it_companies)-3:])

print(it_companies[:len(it_companies)//2] + it_companies[len(it_companies)//2+1:])

it_companies.pop(0)
print(it_companies)

it_companies.pop(len(it_companies)//2)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
tech = front_end + back_end
print(tech)

full_stack = tech.copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python') # +1 of the element insert after. no +1 will insert before the element
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print(full_stack)

# Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print('Min: {}\nMax: {}'.format(ages[0], ages[-1]))

if len(ages) % 2 == 0:
    median = (ages[int(len(ages)/2)] + ages[int(len(ages)/2-1)]) / 2 # follows PEMDAS
else:
    median = ages[int(len(ages)//2)] / 2
print('Median:', median)

average = sum(ages)/len(ages)
print('Average:', average)

print('Range:', ages[-1] - ages[0])

min_ave = abs(ages[0] - average)
max_ave = abs(ages[-1] - average)
print('Absolute Value of min - average:', min_ave)
print('Absolute Value of max - average:', max_ave)
if(min_ave > max_ave):
    print("min - average is greater than max - average")
elif(min_ave < max_ave):
    print("min - average is less than max - average")
else:
    print("min - average is equal to max - average")

print(len(countries))
if len(countries) % 2 == 0:
    print('Middle countries: {}, {}'.format(countries[int(len(countries)/2-1)], countries[int(len(countries)/2)]))
    first_half = countries[:int(len(countries)/2)]
    second_half = countries[int(len(countries)/2):]
    
else:
    print('Middle countries: {}'.format(countries[int(len(countries)//2)]))
    first_half = countries[:len(countries)//2+1]
    second_half = countries[len(countries)//2+1:]

print(first_half)
print(second_half)

other_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = other_countries
print(china)
print(russia)
print(usa)
print(scandic)