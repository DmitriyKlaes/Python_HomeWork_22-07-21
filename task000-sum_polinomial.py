# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# polinomial_1 = ''
import re
# with open('task000-polinomial_1.txt', 'r') as file_1:
#     polinomial_1 = [i for i in reversed(file_1.read()) if i != ' ']
# with open('task000-polinomial_2.txt', 'r') as file_2:
#     polinomial_2 = [i for i in reversed(file_2.read()) if i != ' ']
with open('task000-polinomial_1.txt', 'r') as file_1:
    polinomial_1 = file_1.read().split()
with open('task000-polinomial_2.txt', 'r') as file_2:
    polinomial_2 = file_2.read().split()

print(polinomial_1)
print(polinomial_2)
s = "text text : one two three"
print(s[s.find(":")])
# for i in range(len(polinomial_2)):
#     if polinomial_2[i] == '-':
#         polinomial_2[i - 1] = int(polinomial_2[i - 1]) * -1
    
# print(polinomial_1)
# print(polinomial_2)
    

# dic = {i: x for i, x in zip(reversed(polinomial_1), polinomial_2)}
# print(dic)

str1 = "Python"
dic = {i: x for i, x in enumerate(reversed(str1), 1)}
print(dic)



# print(file_1.writelines)

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }

# for item in dictionary:  # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
    
# print(dictionary)

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# for k in dictionary:
#     print(dictionary[k])

