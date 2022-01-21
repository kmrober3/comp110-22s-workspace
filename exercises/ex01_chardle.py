"""EX01 - Chardle - A cute step twoard Wordle.""" 

__author__ = 730478255 


"""Prompting for inputs"""
word: str = input("Enter a 5-character word: ") 
if len(word) != 5: 
    print("Error: Word must contain 5 characters")  
    exit()
letter: str = input("Enter a single character: ")  
if len(letter) != 1: 
    print("Error: character must be a single character") 
    exit()
print("Searching for " + letter + " in " + word)  


"""Checking indices for matches"""
if word[0] == letter: 
    print(letter + " found at index 0")  
if word[1] == letter: 
    print(letter + " found at index 1") 
if word[2] == letter: 
    print(letter + " found at index 2") 
if word[3] == letter: 
    print(letter + " found at index 3") 
if word[4] == letter: 
    print(letter + " found at index 4")   


"""Counting matching indices """
matching = word.count(letter) 
if matching == 1: 
    print("1 instance of " + letter + " found in " + word)
if matching == 2: 
    print("2 instances of " + letter + " found in " + word) 
if matching == 3: 
    print("3 instances of " + letter + " found in " + word)
if matching == 4: 
    print("4 instances of " + letter + " found in " + word)
if matching == 5:  
    print("5 instances of " + letter + " found in " + word) 
else:
    if matching == 0: 
        print("No instances of " + letter + " found in " + word)  