import json
# importing random for create randome user
from random import randint as rd, choice as ch
# importing pprint for print code beautify
from pprint import pprint

num1 = int(input('num1 '))
num2 = int(input('num2 '))
result = num1 + num2

# write to 
def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)



def read(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return json.load(file)

class User:
    def __init__(self):
        self.id = rd(0, 1000)
        self.name = ch(['first', 'second', 'third'])
        self.age = rd(0, 70)

data = {
    "users": []
}

for i in range(10):
    data['users'].append(User().__dict__)

# input(data)
# s_data = {
#     "users":[num1,num2,result] 
# }

write(data, 'js.json')

n_data = read('js.json')

print(n_data['users'][0]['id'])