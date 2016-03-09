"""
stringjumble.py
Author: Billy
Credit: http://stackoverflow.com/questions/18455222/how-to-count-the-number-of-letters-in-a-string-without-the-spaces, David, Ryan

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

userInput = input("Enter a sentene, word or paragraph.")

"""
for i in range(inputLength):
    for userString[:]:
        print (inputLength)
"""   
        
print(len([userInput]))


from collections import Counter



def count_letters(userInput):
    global count
    inputList = string.split(userInput)
    count = Counter()
    for words in stringList:
        for letters in set(userInput):
            return count[letters]


print (count_letters(userInput))