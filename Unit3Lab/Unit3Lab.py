def schoolAndSubject(): #prints school and subject.
    print('I go to Bellarmine Preparatory School.')
    print('My favorite subject is python.')

def yearsOfSchool(): #prints how many years of school.
    myGrade=input('What grade are you in?')
    yearsInSchool= int(myGrade)*1
    print('You have been going to school for '+str(yearsInSchool) +' years')

def cityGrade(myCity, myGrade): #puts city/grade input into string.
    return('My city is ' + myCity + ' and my grade is ' + myGrade)

def randomNumber(num1, num2): #picks random number in between given start and end values, prints to system.
    return (randint(int(num1), int(num2)))


def boxArea(base, height): #takes base and height values, multiplies them to get the area.
    return(base*height)

def boxPerimeter(base, height): #takes base and height values, multiplies each by two and adds them together to get the perimeter.
    return((2*base)+(2*height))

schoolAndSubject()

yearsOfSchool()

city=input('What city are you from?')
grade=input('What grade are you in?')
myCityAndGrade=cityGrade(str(city),str(grade))
print(myCityAndGrade)

from random import *
start=input('Pick a start value')
end=input('Pick an end value')
ranNumber=randomNumber(int(start), int(end))
print (ranNumber)

x=input('Pick a base value.')
y=input('Pick a height value')
perimeter=boxPerimeter(int(x),int(y))
print('The perimeter is ' +str(perimeter))

area=boxArea(int(x),int(y))
print('The area is ' + str(area))




