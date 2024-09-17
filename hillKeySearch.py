import numpy as np
from numpy.linalg import inv
from math import gcd

def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

def num_to_letter(num):
    return chr((num % 26) + ord('A'))

# Nyari invers modulo 26
def mod_inv(matrix, modulus):
    det = int(round(np.linalg.det(matrix))) 
    if gcd(det, modulus) != 1:
        raise ValueError("Determinan tidak bisa dimod 26, coba input lain")
    
    det_inv = pow(det, -1, modulus) 
    matrix_inv = det_inv * np.round(det * inv(matrix)).astype(int) % modulus
    return matrix_inv

def find_key_matrix(plaintext, ciphertext, matrix_size):
    if len(plaintext) != len(ciphertext):
        raise ValueError("Plaintext dan Ciphertext panjangnya harus sama.")
    
    # Ukuran matriks kunci dengan panjang text harus sesuai
    expected_length = matrix_size * matrix_size  # Contoh: 4 untuk 2x2, 9 untuk 3x3
    if len(plaintext) != expected_length:
        raise ValueError(f"Plaintext dan Ciphertext harus sepanjang {expected_length} karakter untuk matriks {matrix_size}x{matrix_size}")
    
    plaintext_vectors = []
    ciphertext_vectors = []
    
    for i in range(0, len(plaintext), matrix_size):
        plaintext_block = [letter_to_num(c) for c in plaintext[i:i+matrix_size]]
        ciphertext_block = [letter_to_num(c) for c in ciphertext[i:i+matrix_size]]
        
        plaintext_vectors.append(plaintext_block)
        ciphertext_vectors.append(ciphertext_block)
    
    # Blok text jadi matriks
    P = np.array(plaintext_vectors).T  # Transpose
    C = np.array(ciphertext_vectors).T  # Transpose
    
    # Invers modulo 26
    P_inv = mod_inv(P, 26)
    
    # Persamaan matriks kunci
    key_matrix = np.dot(C, P_inv) % 26
    
    return key_matrix

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ").upper().replace(" ", "")
    ciphertext = input("Enter ciphertext *panjangnya harus sama kaya plaintext!: ").upper().replace(" ", "")
    
    matrix_size = int(input("Enter the matrix size (Contoh: 2 untuk 2x2): "))
    
    # Cuma akan ngeproses se-matrix_size^2
    plaintext = plaintext[:matrix_size**2]
    ciphertext = ciphertext[:matrix_size**2]
    
    try:
        key_matrix = find_key_matrix(plaintext, ciphertext, matrix_size)
        print("Key Matrix:")
        print(key_matrix)
    except ValueError as e:
        print(e)
