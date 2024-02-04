from snakes_and_ladders.game import Game
from snakes_and_ladders.helpers.before_game import ask_number_of_players, generate_players


if __name__ == "__main__":
    num_of_players = ask_number_of_players()
    players = generate_players(num_of_players)

    game= Game(players, num_of_players)
    game.play()




