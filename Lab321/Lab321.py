#Brad Bowman
#Python period 5
#Lab321

def main():
    whatGrade = input('What grade are you in?')
    schoolYear = gradeName(whatGrade) #calls gradeName, passes variable 'whatGrade' to function, returned value is assigned to 'schoolYear'.
    print(schoolYear)
    gradeList = []
    grades = input('How many grades?')
    print(grades)
    for x in range (0, int(grades)):
        myGrades = float(input('Give a number grade.')) #turns input into a float so it can be used to calculate the average.
        gradeList.insert(x, myGrades) #puts grades into list.
    print (gradeList)
    average = avgGrade(gradeList) #passes created list to avgGrade function, set equal to a variable.
    print('Your average grade is a ' +str(average) + ' percent.')
    gradeLetter = letterGrade(average)
    print(gradeLetter)
        
    #gradeOne = input('Give a number grade.')
    #gradeTwo = input('Give a number grade.')
    #gradeThree = input('Give a number grade.')
    #gradeFour = input('Give a number grade.')
    #calulatedGrade = avgGrade(int(gradeOne), int(gradeTwo), int(gradeThree), int(gradeFour)) #takes grade input and passes to fourGrades.
    #print('Your average grade is '+ str(calulatedGrade) + '.')
    #gradeLetter = letterGrade(calulatedGrade) #calls letterGrade, passes variable 'calculatedGrade' to function, returned value is assigned to 'gradeLetter'.
    #print(gradeLetter)

def gradeName(yearGrade):
    if yearGrade == str(9):
        return 'You are a freshman.' #prints freshman if the variable 'whatGrade' (which is being passed to the funtion) is equal to 9.
    elif yearGrade == str(10):
        return 'You are a sophmore.' #prints sophmore if the variable 'whatGrade' (which is being passed to the funtion) is equal to 10.
    elif yearGrade == str(11):
        return 'You are a junior.' #prints junior if the variable 'whatGrade' (which is being passed to the funtion) is equal to 11.
    elif yearGrade == str(12):
        return 'You are a senior' #prints senior if the variable 'whatGrade' (which is being passed to the funtion) is equal to 12.
    else:
        return 'You must not be in highschool.'

def avgGrade(list): #puts passed values into list.
    sum = 0.0
    for grades in list:
        sum = sum +grades
    print(sum)
    average = sum/len(list) #divides sum by length of passed list.
    return average

    #averageGrade = (a+b+c+d)/len(gradeList) #adds the input that is being passsed into the function, divides by the length of the list.
    #return averageGrade

def letterGrade(x): #decides letter grade based off of the variable 'calculatedGrade' which is passed into the function.
    if float(x) >= 93:
        return'You have an A!'
    elif float(x) >= 82:
        return 'You have a B!'
    elif float(x) >= 72:
        return 'You have a C!'
    elif float(x) >= 62:
        return 'You have a D!'
    else:
        return 'You need to study harder.'


main() #runs main function defined at beginning of the program.



