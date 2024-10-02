dog = {}
print(dog)

dog['name'] = 'doge'
dog['color'] = 'white'
dog['breed'] = 'dalmatian'
dog['legs'] = 4
dog['age'] = 5
print(dog)

student = {
    'first_name':'Mike',
    'last_name':'Ko',
    'gender':'Male',
    'age':'17',
    'marital status':'Single',
    'skills':['dancing', 'drawing', 'singing'],
    'country':'Philippines',
    'city':'Manila',
    'address':'Taguig City'
}
print(student)

print(len(student))

print(student['skills'])
print(type(student['skills']))

student['skills'].extend(['basketball', 'python'])
print(student['skills'])

print(student.keys())

print(student.values())

student_tuple = student.items()
print(student_tuple)

student.popitem()
print(student)

del student
# print(student)