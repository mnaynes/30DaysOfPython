sentence = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(sentence)

sentence = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(sentence)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[company.find(' ')+1:])
if company.find('Coding') != -1:
    print('Coding is in \'{}\''.format(company))
else:
    print('Coding is not in \'{}\''.format(company))

print(company.replace('Coding', 'Python'))

sentence = 'Python for Everyone'
print(sentence.replace('Everyone', 'All'))

print(company.split())

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

print(company[0])

print(company.rfind(company[-1]))
print(len(company)-1)

print(company[10])

print(company[0] + company[company.find(' ')+1] + company[company.rfind(' ')+1])
print(company[0]+company[7]+company[11])

print(company.index('C'))
print(company.index('F'))

print('Coding For All People'.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))

print(sentence[sentence.index('because'):sentence.rindex('because')+len('because')])

print(sentence.index('because'))

# if company.find('Coding') == 0:
#     print('{} starts with \'Coding\''.format(company))
# else:
#     print('{} does not start with \'Coding\''.format(company))

# print('Coding coding for all coding'.rfind('coding'))
# print(len('Coding for all coding'))
# print('Coding for all coding'.rfind('coding')+len('coding'))
# if company.rfind('coding')+len('coding') == len(company):
#     print('{} ends with \'coding\''.format(company))
# else:
#     print('{} does not end with \'coding\''.format(company))
print(company.startswith('Coding'))
print(company.endswith('coding'))

print('   Coding For All      '.strip())

var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print(var1.isidentifier())
print(var2.isidentifier())

web_tech = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' # '.join(web_tech)
print(result)

print('I am enjoying this challenge.\nI just wonder what is next.')

data = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki' 
print(data.expandtabs(10))

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {:.0f} meters square.'.format(radius, area))

a=8
b=4
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))