n = ["Michael", "Lieberman"]
# Add your function here

#   "words" will be a list
def join_strings(words):
  result = ""
  for i in words:
   result += words[i]  
  return result
  
print (join_strings(n))