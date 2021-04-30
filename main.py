# Original author: Morgan McKinney 4/2021

# Modular exponentiation
def modular_exp(x, y, m):
    return pow(x, y, m)


# Setup keys
# Compute public key
n = 0
e = 0
key_public = [str(n), str(e)]
f = open("public_key.txt", "x")
f.writelines(key_public)
f.close()
# Compute private key
key_private = ""
f = open("private_key.txt", "x")
f.write(key_private)
f.close()

# Encryption
ciphertext = ""
f = open("ciphertext.txt", "x")
f.write(ciphertext)
f.close()

# Decryption
