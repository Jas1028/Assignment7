# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)

# #Steps

#Print the criteria you need to meet
print("\nThings you need to know before you create a password:\n")
print("a. The password should be greater than 15.")
print("b. The password should contains at least one capital letter.")
print("c. The password should contains at least one number.")
print("d. The password should contains at least one special character.")

# List the characters needed
SpecialCharacters = ('~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','<','>',',','.','/','?','"',':',';','|','[',']','{','}',"'")
CapitalLetters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z')
Numbers = ('0','1','2','3','4','5','6','7','8','9')

# Ask the user's password
def CreatePassword():
    Password = input(f"\nPlease Enter Your Password: ")
    return Password
password = CreatePassword()

# Count Variable
ValueCalc = 0
LetterByLetterCount = 0

for character in password:
    LetterByLetterCount = LetterByLetterCount + 1
    if LetterByLetterCount >= 15:
        ValueCalc = True
    else:
        ValueCalc = False

# The program will display if the password is valid or invalid
if LetterByLetterCount > 15:
    if any(character in SpecialCharacters for character in password):
        if any(character in CapitalLetters for character in password): 
            if any (Numbers for character in password):
                 print("Your password is valid. ")
if LetterByLetterCount <= 15 or not any(character in SpecialCharacters for character in password) or not any(character in CapitalLetters for character in password) or not any(Numbers for character in password):
                 print("Invalid Password")
if LetterByLetterCount <= 15:
    AddNumber = int(16 - len(password))
    print(f"You need to add {AddNumber} or more characters.")
if not any(character in SpecialCharacters for character in password):
    print("You didn't put any special character in your password, you should put atleast one. ")
if not any(character in CapitalLetters for character in password):
    print("You didn't put any capital letter in your password, you should put atleast one.")
if not any(character in Numbers for character in password):
    print("You didn't put any number in your password, you should atleast one.")

    
        
