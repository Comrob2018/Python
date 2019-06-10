import argparse

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def wordEncode(word):
    numWord = ''
    for x in word:
        x = x.lower()
        if x in alpha:
            x = alpha.index(x)+1
        else:
            x = 00
        if x < 10:
            numWord += "0"+ str(x)
        else:
            numWord += str(x)
    return numWord
    
def numDecode(word):
    newWord = ''
    numList = [word[i:i+2]for i in range(0, len(word), 2)] ''' Takes the input string and splits it every two characters 
                                                               Then adds the groups to a list''' 
    for num in numList: #iterates through the list to change each number to a letter or space if it is a 00.
        num = int(num) - 1
        if num == -1:
            newWord += ' '
        else:
            newWord += alpha[num]    
    return newWord

def main():
    parser = argparse.ArgumentParser()
    ReqArgs = parser.add_argument_group('required arguments')
    ReqArgs.add_argument("-d", "--decode", help="Decode a numerical string into a non-numerical string", action="store_true")
    ReqArgs.add_argument("-e", "--encode", help="Encode a non-numerical string into a numerical string", action="store_true")
    ReqArgs.add_argument("-w", "--word", help="The string you wish to change, if passing multiple words use quotes", action="store", required=True)
    args = parser.parse_args()

    
    if args.encode: 
        print(wordEncode(args.word))
    elif args.decode:
        print(numDecode(args.word))
    else:
        print('Wrong choice')

if __name__ == "__main__":
    main()
