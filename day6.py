#Getting a string and reversing its words

word="I am a woman"
words=word.split()
start=0
end=len(words)-1
while start<end:
 words[start],words[end]=words[end],words[start]
 start+=1
 end-=1
 new=" ".join(words)
 print(new)

#Checking for a palindrome

word_two="elle"

start=0
end=len(word_two)-1

if word_two[start]==word_two[end]:
 start+=1
 end-=1
 print("palindrome")

else:
    print("Not a palindrome")

    
# Reversing
#   word==word[::-1]