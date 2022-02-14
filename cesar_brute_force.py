def rot(char, shift):
  return chr((ord(char) - ord('A') + shift)%26 + ord('A'))

def caesar_brute_force(cipher_text):
    cipher_text = cipher_text.upper()
    for i in range(26):
        line = ''
        for c in cipher_text:
            line += rot(c, i) if c.isalpha() else c
        print(f'rot{i}:\t{line}')

caesar_brute_force('senha aqui')