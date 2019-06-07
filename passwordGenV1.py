from pyAesCrypto import encryptFile, decryptFile 
     #you must install pyAesCrypto first. pip/pip3 install pyaescrypto
from random import randint
import re
import csv
import os
import sys

chars='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ000111222333444555666777888999__..--@@##$$!!&%&**%'
pattern = r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[:punct:]).*$' 
#Pattern to match at least 8 characters, one number, one lower, one upper, and one special character
keychars='ABCDEFGHIJKLMNOPQRSTUVWXYZ00112233445566778899'
csv.register_dialect('pDialect', delimiter='|')
buffersize = 64 * 2048 #buffer for encryption/decryption

def pword_gen():
    pword=''
    needSpecial()
    needNumber()
    plength()
    while len(pword)<=length:
        if specials and numbers:
            pword+=chars[randint(0,101)]
        elif not specials and numbers:
            pword+=chars[randint(0,81)]
        else:
            pword+=chars[randint(0,51)]
    return pword        

def pass_gen():
    getPurpose()
    plength()
    pword_gen(length)
    return "You're password for "+purpose+' is: '+pword 

def needSpecial():
    specials=input("Do you require special characters? y/n ")
    if 'y' in specials:
        specials=True
    else:
        specials=False
    return specials    

def needNumber():
    numbers=input("Do you require numbers? y/n ")
    if 'y' in numbers:
        numbers=True
    else:
        numbers=False
    return numbers

def multi_pass():
    pwordlist=[['Website','Username','Password']]
    count=0
    number()
    plength()
    getFile()
    pwordfile=open(fileName, 'w')    
    while count<amount:
        pword2=''
        getPurpose()
        getUserName()
        pword2+=purpose+','+uName+','
        pword_gen(length)
        pword2+=pword
        pwordlist.append(pword2.split(','))
        count+=1
    writer=csv.writer(pwordfile, dialect='pDialect')
    for row in pwordlist:
        writer.writerow(row)
    pwordfile.close()
    print("Passwords have been generated, check the file labeled " + fileName)
    return pwordlist

def key_gen():
    getPurpose()
    plength()
    kgen()
    print("Your new key for "+purpose+"is: "+key)

def kgen():
    key=''
    plength()
    while len(key)<length:
        key+=keychars[randint(0,45)]
    return key    

def multi_key():
    keylist=[['Purpose', 'Key']]
    count=0
    number()
    plength()
    getFile()
    keyfile=open(fileName, 'w')
    while count<amount:
        key2=''
        getPurpose()
        key2+=purpose+','
        kgen(length)
        key2+=key
        keylist.append(key2.split(','))
        count += 1
    writer=csv.writer(keyfile, dialect='pDialect')            
    for row in keylist:
        writer.writerow(row)
    keyfile.close()
    print("Your keys have been generated, check the file labeled " + fileName)

def pin_gen():
    pin=''
    plength()
    while len(pin)<=length:
        pin+=str(randint(0,9))
    print("Your new pin is: "+pin)
    return pin

def multi_pin():
    pinlist=[]
    count=0
    number()
    plength()
    getFile()
    pinfile=open(fileName, 'w')
    while count<amount:
        pin=''
        while len(pin)<=length:
            pin+=str(randint(0,9))
        pinlist.append(pin)
    pinfile.write(str(pinlist))
    pinfile.close()
    print("Your pins have been generated, check the file labeled " + fileName)

def generate():
    pgen=input("Would you like to generate a password? y/n ")
    if 'y' in pgen:
        pgen=True
    else:
        pgen=False
    return pgen

def multigen():
    mgen=input("Would you like to generate multiple? y/n ")
    if 'y' in mgen:
        mgen=True
    else:
        mgen=False               
    return mgen

def number():
    amount=int(input("Please enter the desired amount: "))
    return amount

def plength():
    length=int(input("Please enter the desired length: "))
    return length

def getFile():
    fileName = input("Please enter the name of the output file: ")
    return fileName

def codekeygen():
    keygen=input("Would you like to generate a code key? y/n ")
    if 'y' in keygen:
        keygen=True
    else:
        keygen=False
    return keygen

def numpin():
    pingen=input("Would you like to generate a numeric PIN? y/n ")
    return pingen

def pass_check(pword):
    print("Checking password...")
    if re.match(pattern, pword):
        print("Password is valid.")
    else:
        print("Password is not valid.")
    return "Password checking complete."    
        
def multi_checker(pwordlist):
    pwordlist=pwordlist[1:]
    print("Checking passwords now...")
    for x in pwordlist:
        if re.match(pattern, x[2]):
            print(x[2]+" is a valid password.")
        else:
            print(x[2]+" is not a valid password.")      
    return "Password checking complete."

def getPurpose():
    purpose = input("Please enter the name of the website this is for: ")
    return purpose

def getUserName():
    uName=input("Please enter your user name for this website: ")
    return uName
    
def pchecker():
    pcheck=input("Would you like to check the password for validity? y/n ")
    if 'y' in pcheck:
        pcheck=True
    else:
        pcheck=False
    return pcheck

def fileEncryptor(fileName):
    length = 20
    getfile = fileName
    key = ''
    for i in range(0, 20):
        key += keychars[randint(0, 45)]
    print("Here is your encryption key: " + key + "\nPlease save this password.")
    encryptedfile = getfile + ".aes"
    encryptFile(getfile, encryptedfile, key, buffersize)
    os.remove(getfile)
    print("Your file has been encrypted as " + encryptedfile + '.')
    
def fileDecryptor():
    getfile = input("Please enter the name of the encrypted file: ")
    key = input("Please enter the key used to encrypt the file: ")
    decryptedfile = "decryptedfile.txt" 
    decryptFile(getfile, decryptedfile, key, buffersize)
    print("Your file has been decrypted as " + decryptedfile + '.')    

def encryption():
    encrypt= input("Would you like to encrypt your file? y/n ")
    if 'y' in encrypt:
        encrypt = True
    else:
        encrypt = False
    return encrypt    
    
def main():
    generate()
    if pgen:
        multigen()
        if mgen:
            print(multi_pass())
            pchecker()
            if pcheck:
                print(multi_checker(pwordlist))
            encryption()
            if encrypt:
                fileEncryptor(fileName)            
        elif not mgen:
            plength()
            print(pass_gen())
            pchecker()
            if pcheck:
                print(pass_check(pword))
    elif not pgen:
        codekeygen()
        if keygen':
            multigen()
            if mgen:
                number()
                plength()
                print(multi_key())
                encryption()
                if encrypt:
                    fileEncryptor(fileName) 
            elif not mgen:
                plength()
                print(key_gen())
        elif not keygen:
            numpin()
            if pingen:
                multigen()
                if mgen:
                    number()
                    plength()
                    print(multi_pin())
                    encryption()
                    if encrypt:
                        fileEncryptor(fileName) 
                if not mgen:
                    plength()
                    print(pin_gen())
        else:
            decrypt = input("Would you like to decrypt a file? y/n ")
            if 'y' in decrypt:
                fileDecryptor()
    else:
        print("Goodbye")

if __name__=='__main__':
    main()
