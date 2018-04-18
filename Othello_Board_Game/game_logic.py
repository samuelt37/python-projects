#Samuel Tse 20893002
#game logic


class Game:
    def __init__(self, rows, columns, turn, corner, win):
        self.rows = rows
        self.columns = columns
        self.turn = turn
        self.corner = corner
        self.win = win
        self.board = self.create_board(self.rows, self.columns, self.corner)
        

#basic functions
    def switch(self, color):
        if color[0] == 'w':
            return 'b'
        elif color[0] == 'b':
            return 'w'
        

    def place(self, rows, columns, color):
        self.board[int(rows)][int(columns)] = color[0]
        

    def next_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'


    def count(self):
        white = 0
        black = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column] == 'w':
                    white += 1
                elif self.board[row][column] == 'b':
                    black += 1
        return(white, black)

    def show_score(self):
         score = self.count()
         return('White: {}\t Black: {}'.format(score[0], score[1]))
            

#creates starting board
            
    def create_board(self, rows, columns, corner):
        board = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append('.')
            board.append(row)
        self.board = board
        self.place_start(corner)
        return(self.board)

    def place_start(self, color):
        self.place(self.rows/2 - 1, self.columns/2, self.switch(color))
        self.place(self.rows/2, self.columns/2, color)
        self.place(self.rows/2 - 1, self.columns/2 - 1, color)
        self.place(self.rows/2, self.columns/2 - 1, self.switch(color))

#determine winner
    def determine_winner(self):
        score = self.count()
        if self.win == 'few':
            if score[0] < score[1]:
                return('White wins!')
            elif score[1] < score[0]:
                return('Black wins!')
            else:
                return('It is a tie')
        else:
            if score[0] > score[1]:
                return('White wins!')
            elif score[1] > score[0]:
                return('Black wins!')
            else:
                return('It is a tie')
        
#check if the tile is valid
    def valid(self, row, column, color):
        flip = []
        if self.board[row][column] == '.':
            flip.append(self.flip_top(row, column, color))
            flip.append(self.flip_bottom(row, column, color))
            flip.append(self.flip_left(row, column, color))
            flip.append(self.flip_right(row, column, color))
            flip.append(self.flip_top_left(row, column, color))
            flip.append(self.flip_top_right(row, column, color))
            flip.append(self.flip_bottom_right(row, column, color))
            flip.append(self.flip_bottom_left(row, column, color))
            return(flip)
        else:
            return(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])

#place piece
    def place_piece(self, row, column, color, valid_move):
        if valid_move != ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']:
            for direction in valid_move:
                if direction == 'top':
                    self.flip_top(row, column, color)
                elif direction == 'bottom':
                    self.flip_bottom(row, column, color)
                elif direction == 'left':
                    self.flip_left(row, column, color)
                elif direction == 'right':
                    self.flip_right(row, column, color)
                elif direction == 'top left':
                    self.flip_top_left(row, column, color)
                elif direction == 'top right':
                    self.flip_top_right(row, column, color)
                elif direction == 'bottom right':
                    self.flip_bottom_right(row, column, color)
                elif direction == 'bottom left':
                    self.flip_bottom_left(row, column, color)
            self.place(row, column, color)
            
        else:
            raise NameError
        
        
#flip tile functions    
    def in_table(self, row, column):
        if 0 <= row and row < self.rows and 0 <= column and column < self.columns:
            return True
        else:
            return False

    
    def flip_top(self, row, column, color):
        count = 0
        while True:
            row = row - 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'top'
                else:
                    return 'x'
            else:
                return 'x'
                

    def flip_bottom(self, row, column, color):
        count = 0
        while True:
            row += 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'bottom'
                else:
                    return 'x'
            else:
                return 'x'

    def flip_left(self, row, column, color):
        count = 0
        while True:
            column = column - 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'left'
                else:
                    return 'x'
            else:
                return 'x'

    def flip_right(self, row, column, color):
        count = 0
        while True:
            column += 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'right'
                else:
                    return 'x'
            else:
                return 'x'

    def flip_top_left(self, row, column, color):
        count = 0
        while True:
            row = row - 1
            column = column - 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'top left'
                else:
                    return 'x'
            else:
                return 'x'

    def flip_top_right(self, row, column, color):
        count = 0
        while True:
            row = row - 1
            column += 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'top right'
                else:
                    return 'x'
            else:
                return 'x'

    def flip_bottom_right(self, row, column, color):
        count = 0
        while True:
            row += 1
            column += 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'bottom right'
                else:
                    return 'x'
            else:
                return 'x'

    def flip_bottom_left(self, row, column, color):
        count = 0
        while True:
            row += 1
            column = column - 1
            if self.in_table(row, column) == True:
                if self.board[row][column] == self.switch(color):
                    self.board[row][column] = color[0]
                    count = 1
                elif self.board[row][column] == color[0] and count == 1:
                    return 'bottom left'
                else:
                    return 'x'
            else:
                return 'x'

                    
        
        

