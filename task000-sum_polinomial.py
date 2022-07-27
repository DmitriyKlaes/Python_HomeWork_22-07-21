# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def import_file(name):
    with open(name, 'r') as file_1:
        return [i for i in file_1.read().split()]

def coeff_symbol(pol):
    count = 0
    for i in pol:
        if i == '-' or i == '+':
            pol[count + 1] = pol[count] + pol[count + 1]
            pol.pop(count)
        count += 1

def get_dict(pol):
    for i in range(len(pol)):
        pol[i] = list(reversed(pol[i].replace('^', '').partition("x")))
        if pol[i][1] == 'x' and pol[i][0] == '':
            pol[i][0] = 1
        if pol[i][1] == '' and pol[i][0] == '':
            pol[i][0] = 0
        pol[i].pop(1)
        pol[i] = list(map(int, pol[i]))
    return dict(pol)

def summ_pol(dict1, dict2):
    max_dict = {}
    min_dict = {}
    result = {}
    if len(dict1) > len(dict2):
        max_dict, min_dict = dict1, dict2
    else:
        max_dict, min_dict = dict2, dict1   
    for i in range(len(max_dict)+(len(max_dict)-len(min_dict)) -1, -1, -1):
        if i in min_dict.keys() and i not in max_dict.keys():
            result[i] = min_dict[i]
        else:
            result[i] = (max_dict[i] if i in max_dict else 0) + (min_dict[i] if i in min_dict else 0)
    return result

def simple_polynomial(dict):
    result = ' '
    pow = len(dict) - 1
    while pow >= 0:
        if pow > 1: result = result + str(dict[pow] if pow in dict else 0) + 'x^' + str(pow)
        if pow == 1: result = result + str(dict[pow] if pow in dict else 0) + 'x'
        if pow == 0: result = result + str(dict[pow] if pow in dict else 0)
        if pow > 0: result = result + ' + '
        pow -= 1
    return result.replace(' 1x', ' x').replace(' 0x', ' x').replace('+ 0', '')


file_1, file_2 = import_file('task000-polinomial_1.txt'), import_file('task000-polinomial_2.txt')
coeff_symbol(file_1)
coeff_symbol(file_2) 
dict_1 = get_dict(file_1)
dict_2 = get_dict(file_2)
result_dict = summ_pol(dict_1, dict_2)
print(f'({simple_polynomial(dict_1)}) + ({simple_polynomial(dict_2)})', end=' =')
print(simple_polynomial(result_dict))
