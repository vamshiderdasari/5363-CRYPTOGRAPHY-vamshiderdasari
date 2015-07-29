###############################################
# Name: Vamshider Reddy,Dasari
# Class: CMPS 5363 Cryptography
# Date: 28 July 2015
# Program 2 - Vigenere Cipher
###############################################
import argparse
import sys
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")
    parser.add_argument("-t", "--type", dest="type",help="Encoding / Decoding mode [enc,dec]")

    args = parser.parse_args()

    folder = open(args.inputFile,'r')
    message = folder.read()
    tool = open(args.seed,'r')
    seed = tool.read()
    #here i am taking the seed inside a file which will be more safe.
    key = rv.keywordFromSeed(seed)
    if(args.mode == 'encrypt'):
        result = rv.encrypt(message,key,seed)
        print("The messege has been Encrypted")
    else:
        result= rv.decrypt(message,key,seed)
        print("The messege has been Decrypted")
    o = open(args.outputFile,'w')
    o.write(str(result))


if __name__ == '__main__':
    main()
