sudo = [[6,0,5,0,0,0,0,9,0],
        [0,0,0,0,0,7,0,2,0],
        [1,0,0,0,0,0,0,0,0],
        [0,0,0,9,0,8,0,0,0],
        [0,0,0,0,0,0,5,0,0],
        [4,0,0,0,0,0,1,0,6],
        [0,8,0,0,0,3,0,0,0],
        [0,0,0,5,1,0,0,0,0],
        [0,2,0,0,0,0,0,0,0]]

#Enter number from user 
print(input("Please enter your number:"))
userNumber = input()

# is number can put in row ?
def sudoFunc(row, column, userNumber):
    for i in range(0,9):
        if sudo[row][i] == userNumber:
            return False     
 # is number can put in column ?
    for i in range(0,9):
        if sudo[i][column] == userNumber:
            return False 
# is number can put in square ?



