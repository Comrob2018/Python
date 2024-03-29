#!/usr/bin/env python3
#File encryption/decryption program that accepts command line input. Developed by Robert Hendrickson.
from pyAesCrypt import encryptFile, decryptFile # you must use pip/pip3 install pyAesCrypt if you don't have it installed
from random import choice
import os
import argparse

keychars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ00112233445566778899'
buffersize = 64*2048


def encryptor(filename):
    """
    file encryption, takes in a file name and encrypts it with AES encryption
    """
    key = ''
    for i in range(0, 20): # generates a key for encryption of the file
        key += keychars[choice(keychars)]
    print(f"Here is your encryption key: {password} \nPlease save this password.")
    encryptedfile = f"{filename}.aes"
    encryptFile(filename, encryptedfile, key, buffersize)
    # only use one of the following
    os.rename(filename, f".{filename}") # renames the original file to .file (in linux this will make it "hidden") 
    os.remove(filename) # deletes the file from your computer
    return f"Your file has been encrypted as {encryptedfile}."


def decryptor(filename):
    """
    file decryption, takes in a file name and decrypts it
    """
    key = input("Please enter the key used to encrypt the file: ")
    decryptedfile = "decrypted." + filename
    decryptFile(filename, decryptedfile, key, buffersize)
    return "Your file has been decrypted as " + decryptedfile + '.'
    
    
def dencryptor():
    """
    Syntax: 
    python3 dencryptor2.py -e -f <filename> <-- this will encrypt the file specified
    python3 dencryptor2.py -d -f <filename> <-- this will decrypt the file specified
    """
    parser = argparse.ArgumentParser() # command line argument settings
    ReqArgs = parser.add_argument_group('required arguments')
    ReqArgs.add_argument("-d", "--decrypt", help="Decrypt file", action="store_true")
    ReqArgs.add_argument("-e", "--encrypt", help="Encrypt file", action="store_true")
    ReqArgs.add_argument("-f", "--filename", help="Name of file to encrypt/decrypt", action="store", required=True)
    args=parser.parse_args()
    
    if len(args.filename) <= 0: # checks to ensure a file name was given.
        print("You must enter a filename.") 
    
    if args.encrypt: # checks for encrypt flag
        print(encryptor(args.filename))
    elif args.decrypt: # checks for decrypt flag
        print(decryptor(args.filename))
        
if __name__ == "__main__":
    dencryptor()    
