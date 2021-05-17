def encrypt(key,plaintext):
    uppercase_ASCII = {ascii:chr(ascii) for ascii in range(65,91)}
    #print(uppercase_ASCII)

    if(plaintext.isupper() and plaintext.isalpha()):
        ciphertext=""
        ASCII_values = []
        for character in plaintext:
            current_order = ord(character)
            #print('current order', current_order)
            if current_order not in uppercase_ASCII:
                cipher_order = current_order
            else:
                if current_order in uppercase_ASCII and (current_order + key % 26) in uppercase_ASCII:
                    cipher_order = current_order + key % 26
                else:
                    cipher_order = current_order + key % 26 -26

            ASCII_values.append(cipher_order)
        #print('ASCII', ASCII_values)

        ciphertext = ''.join(chr(i) for i in ASCII_values)
        #print(ciphertext)
        return ciphertext
    else:
        print("Please enter uppercase string only")
        return -1

def decrypt(key,cyphertext):
    uppercase_ASCII = {ascii:chr(ascii) for ascii in range(65,91)}
    #print(uppercase_ASCII)
    if(cyphertext.isupper() and cyphertext.isalpha()):
        plaintext=""
        ASCII_values = []
        for character in cyphertext:
            current_order = ord(character)
            #print('current order', current_order)
            if current_order not in uppercase_ASCII:
                cipher_order = current_order
            else:
                if current_order in uppercase_ASCII and (current_order - key % 26) in uppercase_ASCII:
                    cipher_order = current_order - key % 26
                else:
                    cipher_order = current_order - key % 26 +26

            ASCII_values.append(cipher_order)
        #print('ASCII', ASCII_values)

        plaintext = ''.join(chr(i) for i in ASCII_values)
        #print(plaintext)
        return plaintext
    else:
        print("Please enter uppercase string only")
        return -1



print()
print("encrypt")
print(encrypt(-1, "BASE"))
print("decrypt")
print(decrypt(-1, "AZRD")) #[65, 66, 67]
#[66, 67, 68]

print()
print("encrypt")
print(encrypt(1, "BASE"))
print("decrypt")
print(decrypt(1, "CBTF")) #[65, 66, 67]
#[66, 67, 68]

print()
print("encrypt")
print(encrypt(107, "BASE"))
print("decrypt")
print(decrypt(107, "EDVH")) #[65, 66, 67]
#[66, 67, 68]
