print("Slices can be used on both strings and lists.")
print("We will focus on lists here.")
print()
print("Slice notation is as follows [start:stop:step]")
print()
tensList = ["0","10","20","30","40","50","60","70","80","90","100"]
print ("Here's the list we'll be working with. Let's call it tensList.")
print(tensList)
print ("Note that there are 11 values in the list")
print ("List indexes start at 0: 0=0, 1=10, 2=20 and so forth.")
print()

print("Slices include the value at the 'start' index but do not include the value at the 'stop' index. ")
print("The value at index 2 is omitted: tensList[0:2]")
testList = tensList[0:2]
print(testList)
print("Retrieves all values starting at index 2: tensList[2:]")
testList = tensList[2:]
print(testList)
print()

print("Negative 'stop' goes from the end of the list and works back: tensList[5:-1]")
testList = tensList[5:-1]
print(testList)
print("Another example: tensList[-3:]")
testList = tensList[-3:]
print(testList)
print()

print("The 'step' option can be used to skip values: tensList[0:11:2]")
testList = tensList[0:11:2]
print(testList)
print("Omitting the 'start' value defaults to the beginning of the list: tensList[::2]")
testList = tensList[::2]
print(testList)
print("Or you can skip values starting from index 1: tensList[1:11:2]")
print(testList)
testList = tensList[1:11:2]
print(testList)
print("Omitting the 'stop' value defaults to the end of the list: tensList[1::2]")
testList = tensList[1::2]
print(testList)

print("You can reverse a list using this notation: tensList[::-1]")
testList = tensList[::-1]
print(testList)
print("Or you can reverse step through the list: tensList[::-2]")
testList = tensList[::-2]
print(testList)


