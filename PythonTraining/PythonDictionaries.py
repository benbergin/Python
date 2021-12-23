#Dictionaries are similar to lists but their indexes don't have to be integers.
#Indexes for dictionaries are called keys. A dictionary is a set of key-value pairs.
#Dictionaries are denoted with curly braces {}.
#Dictionaries are unordered, so they can't be sliced like lists.
#Dictionaries can be organized like object properties in OOP
car = {'make':'Tesla','model':'S','year':'2021','color':'red','range':'348','mileage':'582','title':'clean'}
car2 = {'make':'Lucid','model':'air','year':'2021','color':'Eureka Gold','range':'520','mileage':'423','title':'clean'}
print(car)
print(car2)

#You can print a dictionary's keys and values follows:
print('Keys: ')
for k in car.keys():
    print(k)
print()
print('Values: ')
for v in car.values():
    print(v)
print()
print("Key-value pairs: ")
for k, v in car.items():
    print('Key: ' + k + ' | Value: ' + str(v))
print()

# setdefault() checks to see if the key exists. If it does exist, then it returns the value,
# otherwise it sets the value to the second parameter if a value is set.
car.setdefault('0-60','2.07')

print(car)

print(car2.setdefault('test'))
print(car2)
print(car2.setdefault('mileage'))
print(car2)
print()
# get() returns the value for the key specified,
# or it returns the default value set in the second parameter if the key does not exist.
print('The Tesla Model S goes 0-60 in ' + car.get('0-60','NA') + ' seconds.')
