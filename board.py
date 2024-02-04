from snakes_and_ladders.helpers.colouredText import colouredText
import random

class Board:
    def __init__(self, player_num=2):
        self.player_num = player_num
        self.BOXWIDTH = 20
        self.snakes, self.ladders = self._generate_snakes_and_ladders()
        self.board = self.createBoard()

    def createBoard(self):
        board = {}
        snakes, ladders = self.snakes, self.ladders

        for row in range(10):
            row_of_boxes = {
                "box_number": [colouredText(0, "blue") for col in range(10)],
                "ladder/snake": [colouredText("", "red") for col in range(10)],
                "ladderrise/snakefall": [colouredText("", "red") for col in range(10)],
            }

            for i in range(self.player_num):
                row_of_boxes[f"player{i + 1}"] = [colouredText("", "white") for col in range(10)]

            # fill numbers
            for col in range(10):
                num = self._generate_number(row, col)
                row_of_boxes["box_number"][col].set_text(num)

            # fill snakes
            for head in snakes:
                if row == head[0]:
                    head_col = head[1]
                    row_of_boxes["ladder/snake"][head_col].set_text("SNAKE!")

                    tail_pos = snakes[head]
                    tail_box_num = self._generate_number(tail_pos[0], tail_pos[1])
                    row_of_boxes["ladderrise/snakefall"][head_col].set_text(f"Fall to box {tail_box_num}")

            # fill ladders
            for bottom in ladders:
                if row == bottom[0]:
                    bottom_col = bottom[1]
                    row_of_boxes["ladder/snake"][bottom_col].set_text("LADDER!")
                    row_of_boxes["ladder/snake"][bottom_col].set_colour("green")

                    top_pos = ladders[bottom]
                    top_box_num = self._generate_number(top_pos[0], top_pos[1])
                    row_of_boxes["ladderrise/snakefall"][bottom_col].set_text(f"Rise to box {top_box_num}")
                    row_of_boxes["ladderrise/snakefall"][bottom_col].set_colour("green")

            board[row] = row_of_boxes

        return board

    def _generate_number(self, row, col):
        if row % 2:
            box_num = 10 * row + (10 - col)
        else:
            box_num = 10 * row + (col + 1)

        return box_num

    def _getRowCol(self, position):
        row = (position - 1) // 10
        if row % 2:
            col = 10 - (position - 10 * row)
        else:
            col = (position - 1) - 10 * row

        return row, col

    def _generate_snakes_and_ladders(self):
        snakes = {}
        ladders = {}

        for snake in range(5):
            snake_head_row = random.randint(1, 9)
            snake_head_col = random.randint(0, 9)
            snake_tail_row = random.randint(0, snake_head_row-1)
            snake_tail_col = random.randint(0, 9)

            snakes[(snake_head_row, snake_head_col)] = (snake_tail_row, snake_tail_col)

        for ladder in range(5):

            unique = False
            while not unique:
                ladder_bottom_row = random.randint(0, 8)
                ladder_bottom_col = random.randint(0, 9)
                ladder_top_row = random.randint(ladder_bottom_row+1, 9)
                ladder_top_col = random.randint(0, 9)

                if (ladder_bottom_row, ladder_bottom_col) not in snakes.keys() and \
                   (ladder_bottom_row, ladder_bottom_col) not in snakes.values() and \
                   (ladder_top_row, ladder_top_col) not in snakes.keys() and \
                   (ladder_top_row, ladder_top_col) not in snakes.values():
                    unique = True

            ladders[(ladder_bottom_row, ladder_bottom_col)] = (ladder_top_row, ladder_top_col)

        return snakes, ladders

    def addPlayer(self, player):
        position = player.get_position()
        row, col = self._getRowCol(position)

        player_num = player.get_player_num()
        player_name = player.get_name()
        player_colour = player.get_colour()

        self.board[row][f"player{player_num+1}"][col] = colouredText(player_name, player_colour)

    def removePlayer(self, player):
        position = player.get_position()
        row, col = self._getRowCol(position)

        player_num = player.get_player_num()

        self.board[row][f"player{player_num + 1}"][col] = colouredText("", "white")

    def check_snake_ladder(self, player):
        position = player.get_position()
        row, col = self._getRowCol(position)

        snakes, ladders = self.snakes, self.ladders

        if (row, col) in snakes:
            idx_to_move = snakes[(row, col)]
            pos_to_move = self._generate_number(idx_to_move[0], idx_to_move[1])
            return ["snakes", pos_to_move]
        elif (row, col) in ladders:
            idx_to_move = ladders[(row, col)]
            pos_to_move = self._generate_number(idx_to_move[0], idx_to_move[1])
            return ["ladders", pos_to_move]

        return None

    def _displayFormattedText(self, colouredtext):
        text = colouredtext.get_text()
        colour = colouredtext.get_colour()

        formattedText = str(text).center(self.BOXWIDTH)
        return colouredText(formattedText, colour)

    def display(self):
        board = self.board
        for key in range(9, -1, -1):
            row = board[key]
            print( ("|" + "-" * self.BOXWIDTH) * 10 )

            keys = ["box_number", "ladder/snake", "ladderrise/snakefall"]
            for i in range(self.player_num): keys.append(f"player{i + 1}")

            for key in keys:
                for col in range(10):
                    print("|", end = '')
                    print(self._displayFormattedText(row[key][col]), end='')
                print("|")

        print( ("|" + "-"*self.BOXWIDTH )*10 + "|")

