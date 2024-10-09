# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(it_companies)
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['FactSet', 'Fujitsu', 'Accenture'])
print(it_companies)

it_companies.remove('Fujitsu')
print(it_companies)

# remove() returns an error when removing an item does not exist in the set
# while discard() does not return an error even even if the item does not exist in the set

print(A)
print(B)
AB = A.union(B)
print(AB)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

AB = A.union(B)
BA = B.union(A)
print(AB)
print(BA)

print(A.symmetric_difference(B))

del AB
del BA

age_set = set(age)
print(age_set)

# string is a list of characters
# list is an ordered and mutable group of elements
# tuple is an ordered and immutable group of elements
# set is an unordered and immutable group of unique elements

sentence = 'I am a teacher and I love to inspire and teach people.'
unique_words = set(sentence.split())
print(unique_words)