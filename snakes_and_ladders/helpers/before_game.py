from snakes_and_ladders.player import Player

def ask_number_of_players():

    valid = False
    print("Number of players supported: 2-4")

    while not valid:
        num = input("Enter the number of players that will be playing: ")

        try:
            num = int(num)
            if not 2 <= num <= 4:
                print("Please enter an integer between 2 and 4")
            else:
                valid = True
        except:
            print("Please enter an integer")

    return num

def generate_players(num_of_players):

    colours = ["purple", "yellow", "cyan", "white"]
    players = []

    for player_num in range(num_of_players):
        print("-----------------------------------------------------------------------------")

        print(f"Player {player_num+1}:")
        name = input("What is your name? ")
        print()
        print(f"Available Colours: {colours}")

        valid = False
        while not valid:
            colour = input("Please choose a colour.")
            colour = colour.lower()

            if colour not in colours:
                print("Please choose a valid, available colour.")
                print()
            else:
                print("Colour registered!")
                colours.remove(colour)
                valid = True

        players.append(Player(name, player_num, colour))

    return players


