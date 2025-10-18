def mutual_prime(a, b):
    while b != 0:
        a, b = b, a%b
    if a == 1:
        return True
    else:
        return False

print(mutual_prime(13, 17))