#Check if the first and last number of a list is the same
list = []
number = int(input("How Many Number You Enter In List: "))
for i in range(0, number):
  list.append(input("Enter a numbers: ").split())

first = list[0]
last = list[-1]

if (first == last):
  print("The First Number", first, "And Last Number", last, "Are same")
else:
  print("The First Number", first, "And Last Number", last, "Are Not Same")
