input_string= input('Enter Your Password = ') 
def printStrongNess(input_string):
    n = len(input_string)
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
     
    for i in range(n):
        if input_string[i].islower():
            hasLower = True
        if input_string[i].isupper():
            hasUpper = True
        if input_string[i].isdigit():
            hasDigit = True
        if input_string[i] not in normalChars:
            specialChar = True
 
    # Strength of password
    print("Strength of password = ", end = "")
    if (hasLower and hasUpper and
        hasDigit and specialChar and n >= 8):
        print("Strong")
         
    elif ((hasLower or hasUpper) and
          specialChar and n >= 6):
        print("Moderate")
    else:
        print("Weak")
if __name__=="__main__":
    printStrongNess(input_string)