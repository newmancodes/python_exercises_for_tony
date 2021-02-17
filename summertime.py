temperature = int(input('Enter temperature: '))
is_summer = input('Is it summer: ').title() == "True"

lower_bound = 25
upper_bound = 30

if is_summer:
    upper_bound = 40

if temperature >= lower_bound and temperature <= upper_bound:
    print('true')
else:
    print('false')