# reading puzzle from txt file :
puzzle = open("puzzle.txt", "r")
print(puzzle.read())

# Enter number from user
print(input("Please enter your number:"))
userNumber = input()  # the number we should predict to fill the cell

# is number can put in row ?
def sudoFunc(row, column, userNumber):
    for i in range(0, 9):  # itrate  row if the number is present it would return false
        if puzzle[row][i] == userNumber:
            print("false-------")
            return False
 # is number can put in column ?
    for i in range(0, 9):  # if the number we enter already present in the particular column it would return false
        if puzzle[column][i] == userNumber:
            print("false")
            return False

# is my solution to itrate row and column true ?









