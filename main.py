# Original author: Morgan McKinney 4/2021

from random import randrange


# Modular exponentiation
def modular_exp(x, y, m):
    print("MODULAR_EXP")
    z = 1
    y_str = str(y)
    for i in y-1:
        z = (z ** 2) % m
        if y_str[i] == 1:
            z = (z * x) % m
    print("Actual:", z)
    print("Expected:", pow(x, y, m))
    return z


# Miller-Rabin primality test
def primality_test(x):
    return x


# Large prime generator
def large_prime(y):
    prime_int = 0
    prime = False
    while not prime:
        # Pick a random, large, and odd number
        large_int = randrange(2 ** (y - 1), 2 ** y)
        if large_int % 2 == 0:  # If number is even
            large_int += 1
        if primality_test(large_int):
            prime_int = large_int
            prime = True
    return prime_int


# Setup keys
# Compute public key
message = open("message.txt", "r").read()
message = int(message)
n = 0
e = 0
# p and q must be 100 decimal digits each, with a difference of at least 10^95
p = large_prime(334)  # 2^333 has 100 digits
q = large_prime(1000)  # 2^999 has 301 digits
n = p * q
key_public = [str(n), str(e)]
print("Public Key: (n, e) =", *key_public)
f = open("public_key.txt", "w")
f.writelines(key_public)
f.close()
# Compute private key
key_private = ""
print("Private Key:", key_private)
f = open("private_key.txt", "w")
f.write(key_private)
f.close()

# Encryption
# Note: We already have the message from the key setup
key_public = open("public_key.txt", "r").read()
ciphertext = ""
print("Message:", message)
print("Ciphertext:", ciphertext)
f = open("ciphertext.txt", "w")
f.write(ciphertext)
f.close()

# Decryption
# Note: We already have the public key from the encryption step
ciphertext = open("message.txt", "r").read()
key_private = open("private_key.txt", "r").read()
decrypted_message = ""
print("Decrypted message:", decrypted_message)
f = open("decrypted_message.txt", "w")
f.write(decrypted_message)
f.close()
