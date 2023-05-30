def pig_latin(text):
  say = ""
  # Separate the text into words
  words = say.split(' ')
  new_words = [f'{word[1:]}{word[0]}ay' for word in words]
  say = ' '.join(new_words)
  #for word in words:
    # Create the pig latin word and add it to the list
  #  say += 
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"