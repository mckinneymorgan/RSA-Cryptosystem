# Original author: Morgan McKinney 4/2021

from random import randrange


# Modular exponentiation
def mod_exp(x, y, m):
    # Input: Integers x, y, and m
    # Output: x^y (mod m)
    z = 1
    # Ensure that x <= m
    if x >= m:
        x = x % m
    while y > 0:
        x = (x ** 2) % m
        y = y // 2
        if y % 2 == 1:
            z = (z * x) % m
            y -= 1
    z = z % m
    return z


# Fermat primality test
def primality_test(x):
    # Input: Large integer x
    # Output: Boolean indicating if x is prime
    prime = True
    for i in range(5):
        # Choose random integer a with 1 < a < x
        a = randrange(1, x)
        # If a^(x - 1) != 1 (mod x), x is composite
        if mod_exp(a, x - 1, x) != 1:
            prime = False
    return prime


# Large prime generator
def large_prime(y):
    # Input: Integer y, the power of the large prime
    # Output: Large prime integer, prime_int
    prime_int = 0
    prime = False
    while not prime:
        # Pick a random, large, and odd number
        large_int = randrange(2 ** (y - 1), 2 ** y)
        if large_int % 2 == 0:  # If number is even, make odd
            large_int += 1
        # Check that number is prime
        if primality_test(large_int):
            prime_int = large_int
            prime = True
    return prime_int


# Euclidean Algorithm
def ea(a, b):
    # Input: Integers a and b
    # Output: gcd(a, b)
    if b == 0:
        return a
    return ea(b, a % b)


# Extended Euclidean Algorithm
def eea(a, b):
    # Input: Integers a and b
    # Output: Multiplicative inverse a^(-1) (mod b)
    x, y = 1, a
    x_previous, y_previous = 0, b
    while y != 0:
        x_previous, x = x, x_previous - (b / a) * x
        y_previous, y = y, y_previous - (b / a) * y
    x_previous = x_previous + b
    return x_previous


# Setup keys
# Compute public key
e = 65537  # Typically a good choice (2^16 + 1)
e_exp = 16  # Exponent of e
# p and q must be 100 decimal digits each, with a difference of at least 10^95
p = large_prime(334)  # 2^333 has 100 digits
q = large_prime(667)  # 2^666 has 200 digits
n = p * q
# e must be relatively prime to (p - 1)(q - 1)
relatively_prime = False
product = (p - 1) * (q - 1)
while not relatively_prime:
    if ea(e, product) == 1:
        relatively_prime = True
    # Change e value until it's relatively prime
    else:
        e_exp += 1
        e = 2 ** e_exp + 1
key_public = [str(n), str(e)]
print("Public Key: (n, e) =", *key_public)
f = open("public_key.txt", "w")
f.write("%s\n%s" % (key_public[0], key_public[1]))
f.close()
# Compute private key
key_private = str(eea(e, product))
print("Private Key:", key_private)
f = open("private_key.txt", "w")
f.write(key_private)
f.close()

# Encryption
message = open("message.txt", "r").read()
message = int(message)
key_public = open("public_key.txt", "r").read()
key_public = key_public.splitlines()  # Separate n and e
ciphertext = str(mod_exp(int(message), int(key_public[1]), int(key_public[0])))
print("Message:", message)
print("Ciphertext:", ciphertext)
f = open("ciphertext.txt", "w")
f.write(ciphertext)
f.close()

# Decryption
# Note: We already have the public key from previous module
ciphertext = open("message.txt", "r").read()
key_private = open("private_key.txt", "r").read()
decrypted_message = str(mod_exp(int(ciphertext), int(key_private), int(key_public[0])))
print("Decrypted message:", decrypted_message)
f = open("decrypted_message.txt", "w")
f.write(decrypted_message)
f.close()
