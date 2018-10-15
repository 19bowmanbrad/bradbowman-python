def main():
    myString = str(input('Say something!'))
    print('Your string is- ' + myString)
    print ('Your string without vowels is- ' + noVowels(myString))
    myList = [2,4,6,8]
    multiply = 2
    mathStuff(myList , multiply)



def noVowels(myString):
    myString2 = myString
    myStringDeVoweled = ""
    for vowels in myString2:
        if (vowels != "a" and vowels != "e" and vowels != "i" and vowels != "o" and vowels != "u" and vowels != "A" and vowels != "E" and vowels != "I" and vowels != "O" and vowels != "U" ):
            myStringDeVoweled = myStringDeVoweled + vowels

    return (myStringDeVoweled)

def mathStuff(list, multiply):
    list2 = []
    for i in list:
        math = i * multiply
        list2.insert(i, math)
        print(list2)


main()
