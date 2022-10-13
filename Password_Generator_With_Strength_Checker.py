import random
import array

MAX_LEN =int(input('Enter Password Length = '))
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y',  'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['@', '#', '$', '%']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
 
# randomly select at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
        password = password + x
print(password)

#CheckingProgramStartsFromHere
 
def printStrongNess(password):
    n = len(password)
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
     
    for i in range(n):
        if password[i].islower():
            hasLower = True
        if password[i].isupper():
            hasUpper = True
        if password[i].isdigit():
            hasDigit = True
        if password[i] not in normalChars:
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
    printStrongNess(password)