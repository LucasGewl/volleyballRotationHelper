from makePlayers import makePlayers
from makeRotations import makeRotations

if __name__ == "__main__":
    # make a program that chooses the best possible rotation
    with open("players.json") as json_data:
        players = makePlayers(json_data)
        possibleLineUps = makeRotations(players)
