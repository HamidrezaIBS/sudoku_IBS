
#i was created the board of game and the number of mines
 # but i'm not sure how to put the bomb's
# by random and how can i fill the board ? 


from string import ascii_lowercase

def createBoard(grid):
     gridsize = len(grid)
     
     label = '   '
    #using ascii code from string library to create header of board
     for i in ascii_lowercase[:gridsize]:
        label = label + i + '   '

     print(label + '\n' )

     for index, i in enumerate(grid):
        row = '{0:2}'.format(index + 1)

        for j in i:
            row = row + ' ' + str(j) 

        print(row + '\n')

     print('')



def mineSweeper():
     # try to get size of board & number of mines in board from user :
    board = int(input("please enter the size of board:"))
    mines = int(input("please enter the number of mines:"))
    grid = []
    #fill grid list by ittrating board and number of mines 
    for i in range(board):
       grid.append([])
    for j in range(mines):
        grid[-1].append(0)
     #send grid as argument to createBoard function  
    createBoard(grid)
          
mineSweeper()
