import numpy as np

def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

def num_to_letter(num):
    return chr((num % 26) + ord('A'))

# Buat ngisi yang kosong kalo inputnya gk sesuai kunci
def pad_plaintext(plaintext, matrix_size):
    while len(plaintext) % matrix_size != 0:
        plaintext += 'X'  # Ngisinya pake 'X'
    return plaintext

def hill_cipher_encrypt(plaintext, key_matrix):
    matrix_size = key_matrix.shape[0]
    
    # Ngisi yang kosong kalo ada
    plaintext = pad_plaintext(plaintext, matrix_size)
    
    ciphertext = ""
    
    for i in range(0, len(plaintext), matrix_size):
        # Plaintext jadi matriks
        plaintext_vector = np.array([letter_to_num(c) for c in plaintext[i:i+matrix_size]])
        
        # Ngaliin matriks sama di mod 26
        ciphertext_vector = np.dot(key_matrix, plaintext_vector) % 26
        
        # Angka ke huruf
        ciphertext += ''.join([num_to_letter(num) for num in ciphertext_vector])
    
    return ciphertext

if __name__ == "__main__":
    # Harus simetris
    key_matrix = np.array([[5, 10], [19, 12]])  
    
    # Input plaintext
    plaintext = input("Enter plaintext: ").upper().replace(" ", "")  # Remove spaces
    
    try:
        ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
        print(f"Ciphertext: {ciphertext}")
    except ValueError as e:
        print(e)
