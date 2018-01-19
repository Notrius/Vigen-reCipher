def inputscreen():
    print("To encode a plaintext with a key, enter 1")
    print("To decode a ciphertext with a key, enter 2 ")
    print("To decode a ciphertext with a key length, enter 3")
    print("To decode a ciphertext with statistical analysis, enter 4")
    print()
    print("To exit, enter 5")
import vigenerecipher
def main():

    inputscreen()
    usrinput = int(input())

    while usrinput != 5:
        if(usrinput == 1):
            plaintext = str(input("Please enter the ciphertext. Non-English alphabetic characters are not considered to be encrypted."))
            key = input("Please enter the numerical version of the key. Ex: If your key is ABC, you should enter: 0 1 2").split()
            vigenerecipher.encode(plaintext, key)
            inputscreen()
            usrinput = int(input())
        elif (usrinput == 2):
            ciphertext =  str(input("Please enter the ciphertext. Non-English alphabetic characters are not considered to be encrypted."))
            #key = input("Please enter the numerical version of the key.").split()
            key = [int(x) for x in input("Please enter the numerical version of the key. Ex: If your key is ABC, you should enter: 0 1 2").split()]
            print(key)
            vigenerecipher.decodewithkey(ciphertext, key)
            inputscreen()
            usrinput = int(input())
        elif (usrinput == 3):
            ciphertext = str(input( "Please enter the ciphertext. Non-English alphabetic characters are not considered to be encrypted."))
            keylength = int(input( "Please enter the key length."))
            vigenerecipher.decodewithkeylength(ciphertext, keylength)
            inputscreen()
            usrinput = int(input())
        elif (usrinput == 4):
            ciphertext = str(input("Please enter the ciphertext. Non-English alphabetic characters are not considered to be encrypted."))
            vigenerecipher.decode(ciphertext)
            inputscreen()
            usrinput = int(input())
        else:
            usrinput = int(input("Input is unvalid. PLease enter a valid input."))
    print("Goodbye!")
    return




if __name__ == "__main__":
    main()

