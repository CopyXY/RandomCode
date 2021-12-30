





'''
This the function will move the letter by 10 base off the AVII table.
'''




def crypt(text):
    result = ""


    num = 10 
    
    text = text[::-1]

    for i in range(len(text)):

        word = text[i]

        # Checking if character are uppercase

        if (word.isupper()):
            result += chr((ord(word) + 10 - 65) % 26 + 65)
        else:
            result += chr((ord(word) + 10 - 97) % 26 + 97)
    return result


'''
This the function will reverse the letters by 10 base off the AVII table.
'''

            
def decrypt(text):
    
    result = ""

    text = text[::-1]


    for i in range(len(text)):
        
        word = text[i]

        if (word.isupper()):
            result += chr((ord(word) - 10 + 65) % 26 + 65)
        else:
            result += chr((ord(word) - (10 + 12 ) + 97) % 26 + 97)

    return result


iFile = open("Z:\Python Projects\words.txt", "r") 
oFile = open("encryptedText.txt", "w")
print ("Encrypted:\n")
for text in iFile:
    newTxt = crypt(text.strip()) 
    print (newTxt)
    oFile.write(newTxt + '\n')


iFile.close()
oFile.close()
'''
To read encrypted text from an input file and decrypt it. Then print the decrypted
text to the screen
'''
print ("\nDecrypted:\n")
iFile = open("encryptedText.txt", "r")
for text in iFile:
    print(decrypt(text.strip()))





        

    