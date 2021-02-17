values = input('Enter comma separated list of numbers: ')
numeric_values = list(map(lambda x:int(x), values.split(',')))
print(numeric_values)

def group_lst(lst):
    res = [(el, lst.count(el)) for el in lst]
    return set(res)

unique_numeric_values = list(map(lambda v: v[0], filter(lambda v: v[1] == 1, group_lst(numeric_values))))
if len(unique_numeric_values) == 0:
    print(0)
else:
    sum = 1
    for unique_numeric_value in unique_numeric_values:
        sum = sum * unique_numeric_value
    print(sum)