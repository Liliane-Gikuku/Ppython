#Write a Python program to calculate the length of a string.
def strin(x):

    print(len(x))


strin("Akira")

#2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def numbers(y):
    ss=y.count("a")
    print(ss)
numbers("Anena")

# Write a Python program to get a string made of the 
# first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string

def get_chars(n):
    out=n[0]+n[1]+n[-1]+n[-2]
    print(out)
get_chars("Champion")

#Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', 
# except the first char itself

def change_occurence(x):
    first=x.replace(0,"$")
    for char in x:
        if char==x[0]:
            y=x.replace(index("char"),"$")
            print(y)
            
        elif x[0]:
            x[0]
        print(y)
change_occurence("sources")

def change_char(word):
    for char in word:
        if char==word[0]:
            x=char
            
    y=word.replace(x, '$')
    # str1 = char + word[1:]

    print(y) 

change_char('restart')

def nen(y):
    print(y[1:3])
nen("Akirachix")