def anti_vowel(text):
  anti_vowel_list = []
  newword = ""
  vowelcount = 0

  for char in text:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
      vowelcount += 1
    elif char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
      vowelcount += 1
    else:
      anti_vowel_list.append(char)

  for char in anti_vowel_list:
    newword += (str(char))
  return newword

print (anti_vowel("Hey little goob"))