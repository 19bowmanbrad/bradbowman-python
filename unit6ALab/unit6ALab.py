def dictionary():
    textCodes = {"wbu" : "What about you", "idk" : "I don't know", "ttyl" : "Talk to you later"}
    print (textCodes)
    yesNo = input("Find a text code? -y -n")
    while (yesNo == "y"):
        print(textCodes)
        defCode = input("What code would you like defined?")
        if (defCode in textCodes):
            print (textCodes[defCode])
        if (defCode not in textCodes):
            add(textCodes, defCode)
        changeDelete(textCodes)
        yesNo = input("Would you like to continue? -y -n")


def add(textCodes, defCode):
    add = input("Would you like to add this to the dictionary? -y -n")
    if (add == "y"):
        newCode = defCode
        newMeaning = input("Enter the code's meaning.")
        textCodes[newCode] = newMeaning
        print (textCodes)

def changeDelete(textCodes):
    userEdit = input("Would you like to change or delete code(s)? -c -d -n")
    if (userEdit == "c"):
        whichCode = input("What code would you like to change?")
        print(whichCode)
        newMeaning = input("Enter the code's new meaning.")
        if (whichCode in textCodes):
            textCodes[whichCode] = newMeaning
        else:
            add(textCodes, whichCode)
        print (textCodes)
    if (userEdit == "d"):
        deleteCode = input("Which code do you want to delete?")
        if (deleteCode in textCodes):
            areYouSure = input("Are you sure you want to delete " + deleteCode + " from the dictionary? -y -n")
            if (areYouSure == "y"):
                del textCodes[deleteCode]
        print (textCodes)

dictionary()

