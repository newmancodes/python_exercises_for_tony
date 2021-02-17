for value in range(2, 1001):
    confirmed_prime = True
    for divisor in range(2, value):
        if value % divisor == 0:
            confirmed_prime = False
            break;
    
    if confirmed_prime:
        print(value)