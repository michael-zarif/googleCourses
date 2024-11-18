def pig_latin(text):
  say = ""
  words = text.split(' ') # Separate the text into words
  new_words = [f'{word[1:]}{word[0]}ay' for word in words if word.startswith('h')] # Using List Comprehensions
  say = ' '.join(new_words)
  #for word in words:
    # Create the pig latin word and add it to the list
  #  say += 
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"