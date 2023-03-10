#Print characters from a string that are present at an even index number
word = str(input("Enter A Word: "))
print("The Index Of",word, "Is: ",len(word))
for i in range (len(word)):
  print(word[i])