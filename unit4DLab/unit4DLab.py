def main():
    shoppingCart = [['tooth paste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    allItems = allInOne(shoppingCart)
    print(allItems)



#-------------------------------------------------

def allInOne(myShoppingCart):
    print('allInOne')
    allItem = []
    newList = []
    for item in myShoppingCart:
        for x in item:
            allItem.append(x)
    print(allItem)
    input('pause')
    for x in allItem:
        if x not in newList:
            newList.append(x)


    return newList

#--------------------------------------------------

def countQTips(myShoppingCart):
    print('countQTips')


#---------------------------------------------------
# challenge

def drinkMoreMilk(myShoppingCart):
    print('drinkMoreMilk')


#---------------------------------------------------
# challenge

def mooseCookie(myShoppingCart):
    print('mooseCookie')


#----------------------------------------------------

main()
