import sys
import os
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def cipherText(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 

# This function decrypts the encrypted text and returns the original text 
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 

if __name__ == "__main__":
    msg = input("Please enter the text (Uppercase only): ")
    time = input("Please enter the time of cipher: ")
    fw = open ("output.txt", "a")
    fw.write("The original message is: " + msg + "\n")
    fw.write("The cipher times are: " + time + "\n")
    for i in range(int(time)):
        keyWord = input("Please enter the keyword: ")
        key = generateKey(msg, keyWord)
        cipher_text = cipherText(msg, key)
        print("The original message is " + msg)
        print("The key is " + key)
        print("The cipher is "+ cipher_text)
        fw.write("The key is: " + key + "\n")
        fw.write("The cipher is: " + cipher_text + "\n")
    fw.close()