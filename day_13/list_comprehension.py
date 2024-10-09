numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <= 0])

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([number for row in list_of_lists
                for in_row in row
                    for number in in_row])

row = 10
col = 6
print([(i,) + tuple([i ** j for j in range(col)]) for i in range(row+1)])

ABRV_LEN = 3
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[country.upper(), country[:ABRV_LEN].upper(), capital.upper()] 
            for row in countries
                for country, capital in row])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([{'country': country.upper(), 'city': capital.upper()} 
             for row in countries
                 for country, capital in row])

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([f'{firstname} {lastname}' 
             for name in names
                 for firstname, lastname in name])

print((lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1))(2,3,5,8))
