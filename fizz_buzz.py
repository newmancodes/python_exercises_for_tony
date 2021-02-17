values = input('Enter comma separated list of numbers: ')
numeric_values = list(map(lambda x:int(x), values.split(',')))

result = ''
for value in range(1,31):
    should_fizz = value % numeric_values[0] == 0
    should_buzz = value % numeric_values[1] == 0

    if len(result) > 0:
        result += ','

    if not should_fizz and not should_buzz:
        result += str(value)
    else:
        if should_fizz:
            result += 'Fizz'
        if should_buzz:
            result += 'Buzz'

print(result)