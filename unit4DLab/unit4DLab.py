def main():
    shoppingCart = [['tooth paste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    test = allInOne(shoppingCart)
    print(test)



#-------------------------------------------------

def allInOne(myShoppingCart):
    print('allInOne')
    newList = []
    for item in myShoppingCart:
        if item not in myShoppingCart:
            myShoppingCart.append(item)
    return myShoppingCart

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
