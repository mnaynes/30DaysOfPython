empty_tuple = ()
print(empty_tuple)

brothers = ('rodel', 'joseph')
sisters = ('rosette', 'chacha')

siblings = brothers + sisters
print(siblings)

print('I have {} siblings'.format(len(siblings)))

family_members = list(siblings)
family_members.extend(['delon', 'mercy'])
family_members = tuple(family_members)
print(family_members)

sib1, sib2, sib3, sib4, *parents = family_members
print(parents)

fruits = ('apple', 'orange', 'grape')
vegetables = ('carrot', 'brocolli', 'cabbage')
animal_products = ('milk', 'fur', 'hide')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)

if len(food_stuff_lt) % 2 == 0:
    print(food_stuff_lt[int(len(food_stuff_lt)/2-1):int(len(food_stuff_lt)/2)+1])
else:
    print(food_stuff_lt[int(len(food_stuff_lt)//2)])

print(food_stuff_lt[:3] + food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)