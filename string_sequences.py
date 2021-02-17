string_values = list(input('Enter a comma separated list of strings: ').split(','))
max_found = ''
for start in range(len(string_values[0])):
    for end in range(len(string_values[0][start:])):
        look_for = string_values[0][start:start+end+1]
        if len(look_for) > len(max_found) and look_for in string_values[1]:
            max_found = look_for

print(max_found)