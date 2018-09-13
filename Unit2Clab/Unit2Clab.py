numList=[3,6,9,12,15,18,21,24,27,30]
print(numList)
print(len(numList))
print(numList[0])
print(numList[len(numList)-1])
print(numList[0:5])
subList=numList[0:5]
subList.insert(0,0)
print(subList)
subList.append(33)
print(subList)
subList1=numList+[33]
print(subList1)
myClasses=['AP Computer science', 'Psychology', 'Prayer', 'AP Composition', 'Python', 'Study hall', 'Intro to calculus']
print(myClasses)
myClasses.remove('Prayer')
print(myClasses)
favClass=myClasses.pop(3)
print('My favorite class is ' + favClass)

