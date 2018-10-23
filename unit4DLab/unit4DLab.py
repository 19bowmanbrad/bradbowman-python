def main():
    shoppingCart = [['tooth paste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    allItems = allInOne(shoppingCart)
    print(allItems)
    numQTips = countQTips(shoppingCart)
    print('There are ' + str(numQTips) + ' q-tips in the shopping cart.')
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
    numTips = 0
    for item in myShoppingCart:
        for x in item:
            if x == 'q-tips':
                numTips += 1
    return numTips
#---------------------------------------------------
main()
