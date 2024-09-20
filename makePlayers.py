import json
from typing import TextIO
from player import Player


def makePlayers(json_data: TextIO) -> list[Player]:
    player_info = json.load(json_data)["names"]
    player_list = []
    names = player_info.keys()

    for name in names:
        if player_info[name]["canBlock"] == "True":
            canBlock = True
        else:
            canBlock = False

        position_keys = player_info[name]["positions"].keys()
        possiblePositions = []

        for position_key in position_keys:
            possiblePositions.append(player_info[name]["positions"][position_key])

        if player_info[name]["isSub"] == "True":
            isSub = True
        else:
            isSub = False

        newPlayer = Player(name, canBlock, possiblePositions, isSub)
        player_list.append(newPlayer)

    return player_list
