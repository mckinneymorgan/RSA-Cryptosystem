# Original author: Morgan McKinney 4/2021

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


# Setup keys
# Compute public key
n = 0
e = 0
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
message = open("message.txt", "r").read()
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
