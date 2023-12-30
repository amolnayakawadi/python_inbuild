### List comprehension 
## variable_name = [transformation  iteration  filteration]

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [i**2 for i in list1]
print(list(list2))

data = [2,3,4,5,7,6,8,6,5,7,9,7,2,4,6,7,9]
info = [i**2 for i in data if i%2 == 0]
print(list(info))