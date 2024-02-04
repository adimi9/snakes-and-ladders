from snakes_and_ladders.board import Board
import time

import random

class Game:
    def __init__(self, players, player_num=2):
        self.players = players
        self.player_num = player_num
        self.board = Board(self.player_num)

    def make_move(self, player):

        player_name = player.get_name()
        input(f"{player_name}: Press Enter to Roll the Die")
        num_rolled = random.randint(1, 6)
        print(f"You have rolled {num_rolled}.")

        time.sleep(2)

        prev_pos = player.get_position()
        if prev_pos >= 94:
            spaces_left = 100 - prev_pos
            if num_rolled > spaces_left:
                print("You cannot make a move beyond box 100! Wait for your next turn")
                print()
                return

        self.board.removePlayer(player)

        player.make_move(num_rolled)

        current_pos = player.get_position()
        self.board.addPlayer(player)

        self.board.display()
        print(f"You have moved from box {prev_pos} to box {current_pos}")
        print()

        snakeorladder = self.board.check_snake_ladder(player)
        if snakeorladder:
            self.change_pos(player, snakeorladder)

    def change_pos(self, player, snakeorladder):

        pos_to_move = snakeorladder[1]

        if snakeorladder[0] == "snakes":
            print("Ohno! You have landed right on top of a snake!")
            print(f"You will now fall to box {pos_to_move}")
        else:
            print("You have stumbled across a ladder!")
            print(f"You will now rise to box {pos_to_move}")

        print()
        time.sleep(1)

        self.board.removePlayer(player)
        player.set_position(pos_to_move)
        self.board.addPlayer(player)

        self.board.display()
        print()


    def isGameOver(self):
        for player in self.players:
            if player.get_position() == 100:
                return player.get_name()

        return False

    def play(self):

        while not self.isGameOver():
            for player in self.players:
                self.make_move(player)
                if self.isGameOver():
                    player_won = self.isGameOver()
                    print(f"Congratulations {player_won}! You have reached box 100 first and are the winner!!")
                    print("Yay!!")
                    break
