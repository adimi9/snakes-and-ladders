class colouredText:
    def __init__(self, text, colour):
        self.off = '\x1b[0m'
        self.red = '\x1b[31m'
        self.yel = '\x1b[33m'
        self.grn = '\x1b[32m'
        self.pur = '\x1b[35m'
        self.blue = '\x1b[34m'
        self.cyan = '\x1b[36m'

        self.text = str(text)
        self.colour = colour

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def _generate_colour(self):
        if self.colour == "red":
            return self.red + self.text + self.off

        elif self.colour == "yellow":
            return self.yel + self.text + self.off

        elif self.colour == "green":
            return self.grn + self.text + self.off

        elif self.colour == "purple":
            return self.pur + self.text + self.off

        elif self.colour == "blue":
            return self.blue + self.text + self.off

        elif self.colour == "white":
            return self.text

        elif self.colour == "cyan":
            return self.cyan + self.text + self.off


    def __str__(self):
        return self._generate_colour()

