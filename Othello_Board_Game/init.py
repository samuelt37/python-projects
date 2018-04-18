#Samuel Tse 20893002
#graphics

import game_logic
import copy
import tkinter

DEFAULT_FONT = ('Helvetica', 15)



class Othello_board:
    def __init__(self):
        self._root_window = tkinter.Tk()

        # title
        self._title = tkinter.Frame(
            master = self._root_window, background = '#FFFFFF')

        self._title.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._title_text = tkinter.Label(
            master = self._title,
            text = 'Othello', font = ('Helvetica', 20))

        self._title_text.grid(
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        #main frame
        self._frame = tkinter.Frame(
            master = self._root_window)

        self._frame.grid(
            row = 1, column = 0, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        #game board
        self._board_frame = tkinter.Frame(
            master = self._frame, width = 300, height = 200,
            background = '#000000')

        self._board_frame.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        #Message
        self._message =  tkinter.Frame(
            master = self._frame, background = '#568392')

        self._message.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #Game info
        self._info =  tkinter.Label(
            master = self._message, text = 'Turn',
            background = '#568392', font = DEFAULT_FONT)

        self._info.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #score
        self._score =  tkinter.Label(
            master = self._message, text = 'White: 0\tBlack: 0',
            background = '#568392', font = DEFAULT_FONT)

        self._score.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

        #start
        self._start_frame = tkinter.Frame(
           master = self._frame, background ='#000000')

        self._start_frame.grid(
            row = 1, column = 1,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
            
        self._start = tkinter.Button(
            master = self._start_frame, text = 'Start Game',
            font = DEFAULT_FONT, command = self.start_game)

        self._start.grid(
            row = 0, column = 0)

        #options
        self._num_opt = [4, 6, 8, 10, 12, 14, 16]
        self._color_opt = ['white', 'black']
        
        self._options = tkinter.Frame(
            master = self._frame, background = '#568392')

        self._options.grid(
            row = 0, column = 1,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        self._opt_text = tkinter.Label(
            master = self._options, background = '#568392',
            text = 'Options:', font = ('Helvetica', 17))

        self._opt_text.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #row
        self._row_text = tkinter.Label(
            master = self._options, background = '#568392',
            text = 'Rows:', font = DEFAULT_FONT)

        self._row_text.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._row_opt = tkinter.Spinbox(
            master = self._options, values = self._num_opt,
            width = 5, wrap = True)

        self._row_opt.grid(
            row = 1, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)



        #column
        self._col_text = tkinter.Label(
            master = self._options, background = '#568392',
            text = 'Columns:', font = DEFAULT_FONT)

        self._col_text.grid(
            row = 2, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._col_opt = tkinter.Spinbox(
            master = self._options, values = self._num_opt,
            width = 5, wrap = True)

        self._col_opt.grid(
            row = 2, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        #first
        self._first_text = tkinter.Label(
            master = self._options, background = '#568392',
            text = 'First:', font = DEFAULT_FONT)

        self._first_text.grid(
            row = 3, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._first_opt = tkinter.Spinbox(
            master = self._options, values = self._color_opt,
            width = 5, wrap = True)

        self._first_opt.grid(
            row = 3, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        #corner
        self._corner_text = tkinter.Label(
            master = self._options, background = '#568392',
            text = 'Corner:', font = DEFAULT_FONT)

        self._corner_text.grid(
            row = 4, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._corner_opt = tkinter.Spinbox(
            master = self._options, values = self._color_opt,
            width = 5, wrap = True)

        self._corner_opt.grid(
            row = 4, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #win
        self._win_text = tkinter.Label(
            master = self._options, background = '#568392',
            text = 'Win:', font = DEFAULT_FONT)

        self._win_text.grid(
            row = 5, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._win_opt = tkinter.Spinbox(
            master = self._options, values = ['few', 'most'],
            width = 5, wrap = True)

        self._win_opt.grid(
            row = 5, column = 1, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        

        

        #frame formatting
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._board_frame.rowconfigure(0, weight = 1)
        self._board_frame.columnconfigure(0, weight = 1)

        self._message.rowconfigure(0, weight = 1)
        self._message.columnconfigure(0, weight = 1)

        self._title.rowconfigure(0, weight = 1)
        self._title.columnconfigure(0, weight = 1)

        self._frame.rowconfigure(0, weight = 10)
        self._frame.rowconfigure(1, weight = 1)
        self._frame.columnconfigure(0, weight = 10)
        self._frame.columnconfigure(1, weight = 1)

        self._options.columnconfigure(0, weight = 1)
        self._options.columnconfigure(1, weight = 1)

        self._start_frame.rowconfigure(0, weight = 1)
        self._start_frame.columnconfigure(0, weight = 1)


    #scondary functions
    def start(self):
        self._root_window.mainloop()

        
    def _change_score(self):
        self._score =  tkinter.Label(
            master = self._message, text = self.game.show_score(),
            background = '#568392', font = DEFAULT_FONT)

        self._score.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _change_turn(self):
        text = "{}'s turn".format(self.game.turn)
        self._info =  tkinter.Label(
            master = self._message, text = text,
            background = '#568392', font = DEFAULT_FONT)

        self._info.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def _dis_invalid(self):
        text = "Invalid move, {}'s turn".format(self.game.turn)
        self._info =  tkinter.Label(
            master = self._message, text = text,
            background = '#568392', font = DEFAULT_FONT)

        self._info.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
    def _dis_end(self):
        self._info =  tkinter.Label(
            master = self._message, text = self.game.determine_winner(),
            background = '#568392', font = DEFAULT_FONT)

        self._info.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)




            
    #resize and place tiles on board
    def _draw_board(self, event):
        self._board.delete(tkinter.ALL)

        self._draw_row()
        self._draw_col()
        self._place_tiles()

    def _draw_row(self):
        self.row_coord = []
        for row in range(self.game.rows + 1):
            line = [0, (row / self.game.rows) * self._board.winfo_height(),
                    self._board.winfo_width(),
                    (row / self.game.rows) * self._board.winfo_height()]

            self.row_coord.append(line)

        
        for frac_x1, frac_y1, frac_x2, frac_y2 in self.row_coord:
            self._draw_line(frac_x1, frac_y1, frac_x2, frac_y2)
            
    
    def _draw_col(self):
        self.col_coord = []
        for col in range(self.game.columns + 1):
            line = [(col / self.game.columns) * self._board.winfo_width(), 0,
                    (col / self.game.columns) * self._board.winfo_width(),
                    self._board.winfo_height()]

            self.col_coord.append(line)

            
        for frac_x1, frac_y1, frac_x2, frac_y2 in self.col_coord:
            self._draw_line(frac_x1, frac_y1, frac_x2, frac_y2)


    def _place_tiles(self):
        self.coord_w = []
        self.coord_b = []

        row_num = 0
        for row in self.game.board:
            col_num = 0
            for tile in row:
                if tile == 'w':
                    coord = [self.col_coord[col_num][0],
                             self.row_coord[row_num][1],
                             self.col_coord[col_num + 1][0],
                             self.row_coord[row_num + 1][1]]

                    self.coord_w.append(coord)

                elif tile == 'b':
                    coord = [self.col_coord[col_num][0],
                             self.row_coord[row_num][1],
                             self.col_coord[col_num + 1][0],
                             self.row_coord[row_num + 1][1]]

                    self.coord_b.append(coord)
                col_num += 1
            row_num += 1
            

        for frac_x1, frac_y1, frac_x2, frac_y2 in self.coord_w:
            self._draw_tile(frac_x1, frac_y1, frac_x2, frac_y2, '#FFFFFF')

        for frac_x1, frac_y1, frac_x2, frac_y2 in self.coord_b:
            self._draw_tile(frac_x1, frac_y1, frac_x2, frac_y2, '#000000')


    def _draw_line(self, frac_x1,
                   frac_y1, frac_x2, frac_y2):


        self._board.create_line(
            frac_x1, frac_y1, frac_x2, frac_y2)

    def _draw_tile(self, frac_x1,
                   frac_y1, frac_x2, frac_y2, color):

        self._board.create_oval(
            frac_x1, frac_y1, frac_x2, frac_y2, fill = color)


    #main functions
    def start_game(self):
        self._start = tkinter.Button(
            master = self._start_frame, text = 'New Game',
            font = DEFAULT_FONT, command = self.start_game)

        self._start.grid(
            row = 0, column = 0)
        self.game = p5_game_logic.Game(
            int(self._row_opt.get()), int(self._col_opt.get()),
            self._first_opt.get(), self._corner_opt.get(), self._win_opt.get())

        self._board = tkinter.Canvas(
            master = self._board_frame, background = '#600000')

        self._board.grid(
            row = 0, column = 0, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._board.bind('<Configure>', self._draw_board)

        self._change_score()
        self._change_turn()

        self.play_on_board()

    def check_for_end(self):
        for row in range(self.game.rows):
            for column in range(self.game.columns):
                new_board = copy.deepcopy(self.game)
                valid_move = new_board.valid(row, column, self.game.turn)
                if valid_move != ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']:
                    self.turns_skipped = 0
                    return None

        self.turns_skipped += 1
        
        if self.turns_skipped == 1:
            self.game.next_turn()
            self._change_turn()
            self.check_for_end()
            
        elif self.turns_skipped == 2:
            self._dis_end()
            
        
    
    def play_on_board(self):
        self._board.bind('<Button-1>', self.play_game)


    def play_game(self, event):
        self.check_for_end()
        if self.turns_skipped == 0:
            try:
                self.x_click = int(event.x)
                self.y_click = int(event.y)

                row_num = 0
                for row in self.game.board:
                    
                    if (self.row_coord[row_num][1] <= self.y_click and
                        self.y_click <= self.row_coord[row_num + 1][1]):

                        col_num = 0
                        for column in row:
                            if (self.col_coord[col_num][0] <= self.x_click and
                            self.x_click <= self.col_coord[col_num + 1][0]):

                                
                                test_game = copy.deepcopy(self.game)
                                valid_move = test_game.valid(row_num, col_num,
                                                             self.game.turn)
                                
                                self.game.place_piece(row_num, col_num,
                                                      self.game.turn, valid_move)

                            col_num += 1
                        
                    row_num += 1

                self._place_tiles()
                self._change_score()
                self.game.next_turn()
                self._change_turn()
                self.check_for_end()

    
            except:
                self._dis_invalid()




if __name__ == '__main__':
    Othello_board().start()
