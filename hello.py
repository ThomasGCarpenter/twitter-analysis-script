msg = "Hello Derek"
print(msg)

###################

## list ##
numbers = [1,2,3]

fruits = ['apples', 'oranges', 'grapes', 'pears']

#get a value
print(fruits[1])

#get a length
print(len(fruits))

#append to list
fruits.append('Mangos')

#remove
fruits.remove('grapes')

#insert in position
fruits.insert(2, 'strawberries')

#change value 
fruits[0] = 'blueberries'


## A Tuple is a collection which is ordered and unchangeaable ##
fruits = ('Apples', 'Oranges', 'Grapes')

#single value needs trailing coma
fruits2 = ('Apples',)


## set is a collection which is unordered and unindexed. No Duplicate members.##

#Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#check if in set 
print('Apples' in fruits_set)

## Dictionary ## 

person = {
    'first_name': 'poop',
    'last_name': 'scoop',
    'age': 30
}

#get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# get dict keys 
print(person.keys())

#copy dict
person 2 = person.copy()
person2['city'] = 'Boston'

#list of dict 
people = [
    {'name': 'alsdkjf'},
    {'name': 'laskdjf'}
]

## functions ##

def sayHello(name):
    print(f'hello {name}')

sayHello('Mr Poop')

#return values
def getSum(num1, num2):
    total = num1 + num2
    return total

#lambda function
getSum = lambda num1, num2: num1 + num2

## conditional ##
x = 10
y = 5

if x > y:
    print(f'{x} is greater than {y}')

#if/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print('poop')
 
 if x > 2 and y <= 10:
    print('alkjdsf')

## Membership Operators ## 

numbers = [1,2,3,4,5]

#in
if x in numbers:
    print('something')

if x not in numbers:
    print('something')


## loops ##

people = ['tart', 'fart', 'shart']

for person in people:
    print('something') 

#range
for i in range(0, 11):
    print('something')

#while

count = 0
while count <= 10:
    print('something')


## class ##

class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'my human name is {self.name}'

# Extend Class 
class Customer(User):
    def __init__()

# Init user objet
derek = User('derek', 'derek@derek', 99)