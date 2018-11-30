def main():
    weekends = {"jan" : [6, 7, 13, 14, 20, 21, 27, 28], "feb" : [3, 4, 10, 11, 17, 18, 24, 25], "mar" : [3, 4, 10, 11, 17, 18, 24, 25, 31], "apr" : [1, 7, 8, 14, 15, 21, 22, 28, 29], "may" : [5, 6, 12, 13, 19, 20, 26, 27], "jun" : [2, 3, 9, 10, 16, 17, 23, 24, 30], "jul" : [1, 7, 8, 14, 15, 21, 22, 28, 29], "aug" : [4, 5, 11, 12, 18, 19, 25, 26], "sep" : [1, 2, 8, 9, 15, 16, 22, 23, 29, 30], "oct" : [6, 7, 13, 14 ,20, 21, 27, 28], "nov" : [3, 4, 10, 11, 17, 18, 24, 25], "nov" : [3, 4, 10, 11, 17, 18, 24, 25], "dec" : [1, 2, 8, 9, 15, 16, 22, 23, 29, 30]}
    print(weekends)
    userBirthday = input("What is the month and day of your birthday?")
    month = userBirthday[1:3]
    print (month)
    input("pause")
    convertText(userBirthday)
    print(month)
    print(month.lower())
    for i in weekends:
        print(i)
            # for x in weekends[i]:

def convertText(birthdayDate):
    if  birthdayDate [:1] == "0" or birthdayDate [:1] == "1" or birthdayDate [:1] == "2" or birthdayDate [:1] == "3" or birthdayDate [:1] == "4" or birthdayDate [:1] == "5" or birthdayDate [:1] == "6" or birthdayDate [:1] == "7" or birthdayDate [:1] == "8" or birthdayDate [:1] == "9":
        month = numToMonth(birthdayDate)

    else:
        month = (birthdayDate[:3].lower)
        print(month)

def numToMonth(monthNum):
     if monthNum [:1] == "0":
         numToMonth(monthNum[1:1])

main()



