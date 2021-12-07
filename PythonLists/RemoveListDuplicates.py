guitars = ['Ibanez','Taylor','Taylor','Taylor','Jackson','Taylor','Ibanez','Ibanez','Ibanez','Ibanez','Ibanez','Ibanez','Taylor']
print('Guitars with duplicates:')
print(guitars)
print()
# Remove duplicates from list
def RemoveListDuplicates(theList,doSort=0):
    valCount = 0
    for val in theList:
        valCount = theList.count(val)
        if valCount > 1:
            for i in range(valCount-1):
                theList.remove(val)
    if doSort == 1:
        theList.sort()
    return theList

RemoveListDuplicates(guitars,1)
print('Guitars with duplicates removed:')
print(guitars)

#Dictionaries don't allow duplicates.
#You can remove duplicates simply by converting the list into a dictionary and then back to a list.