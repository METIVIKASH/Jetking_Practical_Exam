# PROGRAM TO PUT EVEN AND ODD ELEMENTS IN A LIST INTO TWO DIFFERENT LISTS
def splitList(userList):
    evenList = []
    oddList = []
    for number in userList:
        if (number % 2 == 0 ):
            evenList.append(number)
        else:
            oddList.append(number)
    print("THE LIST OF ODD NUMBERS ARE :" ,oddList)
    print("THE LIST OF EVEN NUMBERS ARE :",evenList)
userList = [2,5,8,9,11,22,45,33,22,90]
print (" THE USER'S LIST IS : ")
print(userList)
splitList(userList)



