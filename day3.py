def sentence(word):
#   word = "childrenplayingground"
  half_index=len(word)//2
  new = ""

  for indx in  range (len(word)):
    if indx >= half_index:
        new += word[indx].upper()



    else:
      new +=word[indx]

  print(new)

sentence("I am a woman")



    

