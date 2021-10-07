
class Board :
    def __init__(self) :
        self.max_rows = 3
        self.max_columns = 3
        self.board = list([' ' for j in range(self.max_columns)] for i in range(self.max_rows))
    # print(board)

    def display(self):
        print()
        for row in self.board :
            i = 1
            for column in row :
            
                if i%3 == 0:
                    coldata = column
                else : coldata = column +  '|'

                print(coldata,end = "")
                i+=1
            
            print('\n'+'-'*5)

        print()


class player():

    def __init__(self,marker):
        self.marker = marker

    def putmark(self,pos,board):
        row,col = self.compute(pos,board)
        board.board[row][col] = self.marker
               

    def compute(self,pos,board):
        col_pos = (pos - 1 )%board.max_columns
        row_pos = (board.max_rows - 1) - ((pos -1) //board.max_rows)
        
        # print(pos , row_pos,col_pos)
        return row_pos,col_pos

    def checkwin(self,board):
        
        for i in range(board.max_rows):
            if board.board[i][0] == board.board[i][1] == board.board[i][2] == self.marker : return True # horizontal check
            if board.board[0][i] == board.board[1][i] == board.board[2][i] == self.marker : return True # vertical check

        # diagonal check
        if board.board[0][0] == board.board[1][1] == board.board[2][2] == self.marker : return True      
        if board.board[0][2] == board.board[1][1] == board.board[2][0] == self.marker : return True


        return False

    
def game(p1,p2):
    
    player = None
    board = Board()
    won = False
    
    for p in range(1,10):
        if p%2 == 0:
            player = p2
        else :
            player = p1
        
        pos = int(input(f'ENTER POSITION FOR {player.marker} --> '))

        player.putmark(pos,board)
        board.display()
        if player.checkwin(board) : 
            won = True
            print(f"{player.marker} WINS")
            return player

    if not won : print('TIE')


if __name__ == "__main__" :
    game(player("O"),player('X'))
    
