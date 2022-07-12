# Write a Python program to get a single string from two given
#  strings, separated by a space and 
# swap the first two characters of each string

def concat():
   sister="Divine"
   brother="Bonheur"

   new_a=brother[0]+sister[1:]
   new_b=sister[0]+brother[1:]
   new_string=new_a + " "+ new_b
   print(new_string)

concat()


# Write a Python program to add 'ing' at the end of a given string 
# (length should be at least 3). If the given string already ends with 'ing' 
# then add 'ly' instead. If the string length of the given string
#  is less than 3, leave it unchanged
def ing_or_ly(word):
    if len(word)>2:
     if word[-3:]=="ing":
        word+="ly"
     else:  
        word+= "ing"
     
        return word

print (ing_or_ly("go"))

def check(x):
    if x[0:3]!="not":
        new_x="good"
        return new_x

    else:
        return x
print(check("poor not"))


#  Write a Python program to find the first appearance of the substring
#   'not' and 'poor' from a given string, if 'not' follows the 'poor', 
#   replace the whole 'not'...'poor' substring with 'good'. Return the 
#   resulting string


  
        



