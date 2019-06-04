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

def pass_gen(length):
    getPurpose()
    pword_gen(length)
    return "You're password for "+purpose+' is: '+pword 

def pword_gen(length):
    global pword
    pword=''
    while len(pword)<=length:
        if specials=='y'and numbers=='y':
            pword+=chars[randint(0,101)]
        elif specials!='y' and numbers=='y':
            pword+=chars[randint(0,81)]
        else:
            pword+=chars[randint(0,51)]
    return pword        

def needSpecial():
    global specials
    specials=input("Do you require special characters? y/n ")
    if 'y' in specials:
        specials='y'
    else:
        specials='n'
    return specials    

def needNumber():
    global numbers
    numbers=input("Do you require numbers? y/n ")
    if 'y' in numbers:
        numbers='y'
    else:
        numbers='n'
    return numbers

def multi_pass(amount,length):
    global pwordlist
    pwordlist=[['Website','Username','Password']]
    count=0
    pwordfile=open('Passwords.csv', 'w')    
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
    return "Passwords have been generated, check the file labeled Passwords.csv"

def key_gen(length):
    getPurpose()                    
    kgen(length)
    return "Your new key for "+purpose+"is: "+key

def kgen(length):
    global key
    key=''
    while len(key)<length:
        key+=keychars[randint(0,45)]
    return key    

def multi_key(amount,length):
    keylist=[['Purpose', 'Key']]
    count=0
    keyfile=open('Keys.csv', 'w')
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
    return "Your keys have been generated, check the file labeled Keylist.txt"

def pin_gen(length):
    pin=''
    while len(pin)<=length:
        pin+=str(randint(0,9))
    return "Your new pin is: "+pin

def multi_pin(amount,length):
    pinlist=[]
    count=0
    pinfile=open('Pinlist.txt', 'w')
    while count<amount:
        pin=''
        while len(pin)<=length:
            pin+=str(randint(0,9))
        pinlist.append(pin)
    pinfile.write(str(pinlist))
    pinfile.close()
    return "Your pins have been generated, check the file labeled Pinlist.txt"

def generate():
    global pgen
    pgen=input("Would you like to generate a password? y/n ")
    if 'y' in pgen:
        pgen='y'
    else:
        pgen='n'
    return pgen

def multigen():
    global mgen
    mgen=input("Would you like to generate multiple? y/n ")
    if 'y' in mgen:
        mgen='y'
    else:
        mgen='n'                 
    return mgen

def number():
    global amount
    amount=int(input("Please enter the desired amount: "))
    return amount

def plength():
    global length
    length=int(input("Please enter the desired length: "))
    return length

def codekeygen():
    global keygen
    keygen=input("Would you like to generate a code key? y/n ")
    if 'y' in keygen:
        keygen='y'
    else:
        keygen='n'
    return keygen

def numpin():
    global pingen
    pingen=input("Would you like to generate a numeric PIN? y/n ")
    return pingen

def pass_check(pword):
    print("Checking password...")
    if re.match(pattern, pword):
        print("Password is valid.")
    else:
        print("Password is not valid.")
    return "Password checking complete."    
        
def multi_checker(pwordlist, amount):
    pwordlist=pwordlist[1:]
    print("Checking passwords now...")
    for x in pwordlist:
        if re.match(pattern, x[2]):
            print(x[2]+" is a valid password.")
        else:
            print(x[2]+" is not a valid password.")      
    return "Password checking complete."

def getPurpose():
    global purpose
    purpose = input("Please enter the name of the website this is for: ")
    return purpose

def getUserName():
    global uName
    uName=input("Please enter your user name for this website: ")
    return uName
    
def pchecker():
    global pcheck
    pcheck=input("Would you like to check the password for validity? y/n ")
    if 'y' in pcheck:
        pcheck='y'
    else:
        pcheck='n'
    return pcheck

def fileEncryptor():
    length = 20
    getfile = fileName
    password = ''
    for i in range(0, 20):
        password += keychars[randint(0, 45)]
    print("Here is your encryption key: " + password + "\nPlease save this password.")
    encryptedfile = getfile + ".aes"
    encryptFile(getfile, encryptedfile, password, buffersize)
    os.rename(getfile, "."+getfile)
    print("Your file has been encrypted as " + encryptedfile + '.')
    
def fileDecryptor():
    getfile = input("Please enter the name of the encrypted file: ")
    password = input("Please enter the key used to encrypt the file: ")
    decryptedfile = "decryptedfile.txt" 
    decryptFile(getfile, decryptedfile, password, buffersize)
    print("Your file has been decrypted as " + decryptedfile + '.')    

def encryption():
    global encrypt
    encrypt= input("Would you like to encrypt your file? y/n ")
    if 'y' in encrypt:
        encrypt = 'y'
    else:
        encrypt = 'n'
    return encrypt    
    
def main():
    generate()
    if pgen=='y':
        multigen()
        needSpecial()
        needNumber()
        if mgen=='y':
            number()
            plength()
            print(multi_pass(amount,length))
            pchecker()
            if pcheck == 'y':
                print(multi_checker(pwordlist, amount))
            encryption()
            if encrypt == 'y':
                fileEncryptor()            
        elif mgen=='n':
            plength()
            print(pass_gen(length))
            pchecker()
            if pcheck == 'y':
                print(pass_check(pword))
    elif pgen=='n':
        codekeygen()
        if keygen=='y':
            multigen()
            if mgen=='y':
                number()
                plength()
                print(multi_key(amount,length))
                encryption()
                if encrypt == 'y':
                    fileEncryptor() 
            elif mgen=='n':
                plength()
                print(key_gen(length))
        elif keygen=='n':
            numpin()
            if pingen=='y':
                multigen()
                if mgen=='y':
                    number()
                    plength()
                    print(multi_pin(amount,length))
                    encryption()
                    if encrypt == 'y':
                        fileEncryptor() 
                if mgen=='n':
                    plength()
                    print(pin_gen(length))
        else:
            decrypt = input("Would you like to decrypt a file? y/n ")
            if 'y' in decrypt:
                fileDecryptor()
    else:
        print("Goodbye")

if __name__=='__main__':
    main()
