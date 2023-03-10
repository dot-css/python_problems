#sum of the current number and the previous number
num = 0
for i in range (10):
  add = num + 1
  sum = num + add
  print("Current Num is",add,"Pervious Num is",num,"Sum Is",sum)
  num = add