myUniqueList = []
myLeftovers = []


"""
The function addList add the passed content to a list and returns True, if the content already exists it returns False 
The Function also pushes all the non unique content to a garbage collector list (myLeftovers)

"""


def addList(content):
	if content not in myUniqueList:
		myUniqueList.append(content)
		return True
	elif content in myUniqueList:
		myLeftovers.append(content)
		return False
	else:
		pass
		

myname = addList("martin") # Returns True if Unique
addList(10.5) #unique value
addList(15) #unique value
addList("Esther") #unique value
addList(15) # non unique value
addList(200) #unique value
addList(10.5) # non unique value
myOtherName = addList("Esther") 

print(myname) # returns True if the content is successfully added to the list #unique
print(myUniqueList)
print(myLeftovers)
print(myOtherName) # Returns False if not unique



