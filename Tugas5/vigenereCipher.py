def vigenere_encrypt(plaintext, keyword):
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    ciphertext = []
    
    keyword_repeated = ''
    keyword_index = 0
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            keyword_repeated += keyword[keyword_index % len(keyword)]
            keyword_index += 1
        else:
            keyword_repeated += plaintext[i]
    
    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():
            shift = ord(k) - ord('A')
            encrypted_char = chr(((ord(p) - ord('A') + shift) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p)

    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext, keyword):
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    plaintext = []
    
    keyword_repeated = ''
    keyword_index = 0
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            keyword_repeated += keyword[keyword_index % len(keyword)]
            keyword_index += 1
        else:
            keyword_repeated += ciphertext[i]
    
    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():
            shift = ord(k) - ord('A')
            decrypted_char = chr(((ord(c) - ord('A') - shift + 26) % 26) + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c)

    return ''.join(plaintext)

plaintext = "HALO DIANA CANTIK"
keyword = "AP"
ciphertext = vigenere_encrypt(plaintext, keyword)
print("Plain Text:", plaintext)
print("Key:", keyword)
print("Encrypted:", ciphertext)

decrypted_text = vigenere_decrypt(ciphertext, keyword)
print("Decrypted:", decrypted_text)
