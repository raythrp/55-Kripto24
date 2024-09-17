import numpy as np
from numpy.linalg import inv

def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

def num_to_letter(num):
    return chr((num % 26) + ord('A'))

# Nyari invers modulo dulu
def mod_inv(matrix, modulus):
    # Nyari determinan
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    
    matrix_inv = det_inv * np.round(det * inv(matrix)).astype(int) % modulus
    return matrix_inv

def hill_cipher_decrypt(ciphertext, key_matrix):
    matrix_size = key_matrix.shape[0]
    
    inverse_key_matrix = mod_inv(key_matrix, 26)
    
    plaintext = ""
    
    for i in range(0, len(ciphertext), matrix_size):
        # Ciphertext jadi matriks
        ciphertext_vector = np.array([letter_to_num(c) for c in ciphertext[i:i+matrix_size]])
        
        plaintext_vector = np.dot(inverse_key_matrix, ciphertext_vector) % 26
        
        # Angka jadi huruf
        plaintext += ''.join([num_to_letter(int(num)) for num in plaintext_vector])
    
    return plaintext

# Example usage
if __name__ == "__main__":
    # Matriks harus simetris
    key_matrix = np.array([[7, 6], [2, 5]]) 
    
    ciphertext = input("Enter ciphertext: ").upper().replace(" ", "")

    try:
        plaintext = hill_cipher_decrypt(ciphertext, key_matrix)
        print(f"Decrypted Plaintext: {plaintext}")
    except ValueError as e:
        print(e)
