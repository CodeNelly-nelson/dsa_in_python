myList = [11, 3, 23, 7]

myList.append(17)

for index, value in enumerate(myList):
    print(index, value)
    
myList.pop()

for index, value in enumerate(myList):
    print(index, value)
myList.pop(0)

for index, value in enumerate(myList):
    print(index, value)
    
myList.insert(0,11)

for index, value in enumerate(myList):
    print(index, value)
