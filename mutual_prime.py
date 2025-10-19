# Klaviaturadan daxil edilmiş iki natural ədədin rəqəmlərinin hasilinin qarşılıqlı sadə olub olmadığını müəyyən edən proqramı Python dilində yazın.

# Giriş : 34 56
# Çıxış : False

# Giriş : 19 13
# Çıxış : True

def mutual_prime(a, b):
    while b != 0:
        a, b = b, a%b
    if a == 1:
        return True
    else:
        return False
    
def product_digits(x):
    product = 1
    while x>0:
        digit = x % 10
        product *= digit
        x//=10
    return product

a = int(input("Input a: "))
b = int(input("Input b: "))

print(mutual_prime(product_digits(a), product_digits(b)))
