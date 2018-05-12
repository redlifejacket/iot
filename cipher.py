#!/usr/bin/python3
# Shyam Govardhan
# 13 May 2018
# UCI IOT Networking & Security Week 5 Assignmnet

from string import ascii_lowercase

alphabet  = {}
MAX_TRIES = 3

def is_shift_len_valid(shift_len):
    if shift_len >= -26 and shift_len <= 26:
        return True
    else:
        return False

def read_message():
    prompt_message = "Enter message (Press enter to quit):   "
    message = input(prompt_message)
    tries = 0
    while (tries < MAX_TRIES):
        if (message == ""):
            exit()
        else:
            break
        message = input(prompt_message)
        tries += 1
    return message

def read_shift_len():
    shift_len_message = "Enter shift len (Press enter to quit): "
    shift_len = input(shift_len_message)
    tries = 0
    while (tries < MAX_TRIES):
        if (shift_len == ""):
            exit()
        else:
            break
        if (not is_shift_len_valid(int(shift_len))):
            print("Please enter a value less than 26")
        shift_len = input(shift_len_message)
        tries += 1
    return shift_len

def init_alphabet():
    pos = 0
    global alphabet
    for c in ascii_lowercase:
        alphabet[c] = pos
        pos += 1

def get_cipher(char_pos):
    cipher_pos = (char_pos + int(shift_len)) % 26
    char_pos += 1
    return (cipher_pos, ascii_lowercase[cipher_pos])

def get_cipher_text(msg):
    char_pos = 0
    cipher_text = ""
    for char in msg:
        if (ord(char) < 97 or ord(char) > 122):
            cipher_char = char
        else:
            char_pos = alphabet[char]
            (cipher_pos, cipher_char) = get_cipher(char_pos)
        char_pos += 1
        cipher_text += cipher_char
        #print("%s\t%s\t%s\t%s" % (char_pos, char, cipher_char, cipher_pos + 1))
    return cipher_text

# Main Program
init_alphabet()
message = read_message()
shift_len = read_shift_len()
cipher_text = get_cipher_text(message)
print("Cipher text:     [%s]" % cipher_text)
