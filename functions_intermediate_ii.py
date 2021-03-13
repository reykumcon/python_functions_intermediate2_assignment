#1 Update Values in Dictionaries and Lists

x = [ [5, 2, 3], [10, 8, 9] ]

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

#Change the value of 10 in x to 15
x[1][0] = 15
print(x)

#Change last_name of the first student
students[0]['last_name'] = 'Bryant'
print(students[0])

#Change 'Messi' to 'Andres' in sports_directory
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

#Change the value of 20 in z to 30
z[0]['y'] = 30
print(z)

#2 Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        output = ', '.join(' - '.join((key, val)) for (key, val) in some_list[i].items())
        print(output)

iterateDictionary(students)

#3 Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4 Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])

printInfo(dojo)
