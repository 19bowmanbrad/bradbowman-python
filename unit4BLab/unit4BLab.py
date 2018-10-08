for x in range(0,6):
    print(x)
    addTen = (x + 10)
    print ('x plus 10 is ' +str(addTen))
    multiplyTen = (x * 10)
    print('x multiplied by 10 is ' +str(multiplyTen))

myList = [10,20,30,40,50]
print(myList)
for i in (0, len(myList)):
    timesTen = (myList.pop(i) * 10)
    print(timesTen)
    myList.append(timesTen)
    print(myList)
