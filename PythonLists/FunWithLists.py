# Unlike an array, a Python list is a collection of items than can be of varying data types.
# A Python list is denoted with square brackets:
myList = []
# A Python list is mutable meaning you can append items to and remove items from it.
print('Which crypto will rule them all?')
myList.append('Ethereum')
print (myList[0])
print()
print('No, Ethereum is going down!')
myList.remove('Ethereum')
myList.append('Solana')
print(myList[0] + ' will rule!')
print()
print("No one knows, so buy all of these tokens!")
print()
tokensToBuy = ['BTC','ETH','SOL','ALGO','LUNA','DOT','AVAX','KDA','VET','BAT','ENJ','SAND']
print("(Buy list printed as is with no formatting)")
print(tokensToBuy)
print()
# Now, print the tokens using a For loop; add a dollar sign in front of each token
print("(Buy list printed from a For loop that renders the values with a dollar sign added)")
for x in range(len(tokensToBuy)):
    print('$' + tokensToBuy[x])
print()
# Python has a shortcut so you don't have to use a For loop to print a list
# You can use the asterisk character inside of the print function to print just the list values
print("(Buy list printed using the asterisk shortcut and commas to separate the values)")
print(*tokensToBuy, sep = ', ')
print()
# You can also use join within the print function to print the values on a single line
print("(Buy list printed using join with commas to separate the values)")
print(', '.join(tokensToBuy))
print()
# A module called "pretty print" can help with printing objects like lists
print("(Pretty print the buy list)")
from pprint import pprint
pprint(tokensToBuy)
print()

print("Let's ")





# This list has duplicates; write a function to remove the duplicates
cryptoListDups = ['BTC','ETH','ALGO','SOL','ETH','ALGO','BTC','ETH','ALGO','LUNA','DOT']
print('Crypto list with duplicates:')
print(cryptoListDups)
print()
# Remove duplicates from list
def RemoveListDuplicates(theList, doSort = 0) -> object:
    valCount = 0
    for val in theList:
        valCount = theList.count(val)
        if valCount > 1:
            for i in range(valCount-1):
                theList.remove(val)
    if doSort == 1:
        theList.sort()
    return theList

cryptoCleanList = RemoveListDuplicates(cryptoListDups,1)
print('Token list with duplicates removed:')
print(cryptoListDups)

#Dictionaries don't allow duplicates.
#You can remove duplicates simply by converting the list into a dictionary and then back to a list.