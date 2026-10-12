
# def retry(fn, max_attemps=5, base=1, cap=60):
#     return 
from pprint import pprint

numbers = [0,0,2,0,3,7]
lists = [0,0,2,3,7]
letters = ['a', 'b', 'c', 'd']
mixed = [1, 2, 3, 'a', 'b', None, True, False]

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]

extlist = list("there is not a string")
# print(matrix[-1][2])
#print(matrix[2][:2])

# print(numbers.count(0))
# print(numbers.index(2))
# print(letters.index('a'))
#print(lists > numbers)

# letters.insert(0, 'x')
letters[2] = 'm'
#print(letters)

page = dict.fromkeys(['limit', 'offset', 'number'], None)
user = {'id':1, 'name': 'John', 'age': 30, 'city': 'Berlin'}
for key in list(user.keys()):
    if isinstance(user[key], str):  
        user[key] = user[key].upper()
    else: 
        user.pop(key)

print(user)


# matrix[1].append('x')
# matrix[0].insert(0,'y')
# matrix[-1] = ['j','k','l']
# matrix[0][0] = '-'
# matrix[1][1] = '-'
# matrix[2][2] = '-'
# pprint(matrix, width=30)

# removed = letters.pop(0)
# print(letters)
# print('Removed Item:', removed)

# matrix[0].remove('b')
# matrix[-1].pop(0)
# matrix[1].pop()
# pprint(matrix, width=30)

