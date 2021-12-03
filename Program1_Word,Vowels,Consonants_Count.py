# Create a program that ask for a sentence as input
# Display the number of word, vowels and consonants in the input

# Steps

# 1. Ask the user to input sentence and the input will convert into lowercase
SentenceInput = input("Type a sentence: ").lower()

#2 Vowels and consonants list
vowels = ('a','e','i','o','u')
consonants = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
signs = ('.','?',',','-','"','!','(',')',',',':',';','/','&','@','#','*','_',"=",'+')
# If there is a number in sentence
numbers = ('0','1','2','3','4','5','6','7','8','9')

#3 Defining variables
VowelsCount = 0
ConsonantsCount = 0
NumbersCount = 0
SignsCount = 0

#4 Process of counting 
for s in SentenceInput:
    if s in vowels:
        VowelsCount += 1
    else:
        if s in consonants:
            ConsonantsCount += 1
        else:
            if s in numbers:
                NumbersCount += 1
            else:
                if s in signs:
                    SignsCount += 1

# Counting the words in a sentence
def WordCount():
    Words = SentenceInput.split()
    WordC = len(Words)
    return WordC
WordNum = WordCount()

#5 Output of the Program
print("The number of word/s in sentence: ", WordNum)
print("The number of vowel/s in sentence: ", VowelsCount)
print("The number of consonant/s in sentence: ", ConsonantsCount)
print("The number of sign/s in sentence: ", SignsCount)
#If there is a number in sentence
print("The number of number/s in sentence: ", NumbersCount)
