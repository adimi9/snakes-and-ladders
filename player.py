class Player:

    def __init__(self, name, num, colour):
        self.position = 1
        self.name = name
        self.player_num = num
        self.colour = colour

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def set_player_num(self, num):
        self.player_num = num

    def get_player_num(self):
        return self.player_num

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def make_move(self, spaces):
        self.position += spaces

    def __str__(self):
        return f" {self.name} is at position {self.position}"

