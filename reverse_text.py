def reverse(text):
  reverse_list = []
  reverse_var = ""
  for char in range(len(text)):
    charpick = text[(len(text)-(char+1)):len(text)-(char)]
    reverse_list.append(charpick)  

  for char in reverse_list:
    reverse_var += str(char)

  return (reverse_var)

print (reverse("i wish it was better"))