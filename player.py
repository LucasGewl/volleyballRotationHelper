from typing import Optional


class Player:
    """
    A player in volleyball.

    === Public Attributes ===
    name: the players name
    canBlock: can the player block consistently
    positions: the positions the player can play
    isSub: if the player is a sub (not available every game)
    currentPosition: the position the player is in a specific game

    === Representation Invariants ===
    - positions[i] can only be one of the following:
        1. Outside
        2. Opposite
        3. Middle
        4. Libero
        5. Setter
        6. Mid/Lib
        Mid/Lib is for when you want someone to play libero in the back
        but play middle to cover tips in the front, rather than block.
    - currentPosition must be set before each game
    """
    name: str
    canBlock: bool
    positions: list[str]
    currentPosition: Optional[str]

    def __init__(self, name:  str, canBlock: bool, positions: list[str],
                 isSub: bool):
        self.name = name
        self.canBlock = canBlock
        self.positions = positions[:]
        self.currentPosition = None
        self.isSub = isSub

    def setPosition(self, position: str) -> None:
        if position in self.positions:
            self.currentPosition = position
        else:
            raise PlayerDoesntPlayThatException

class PlayerDoesntPlayThatException(Exception):
    pass



# if __name__ == "__main__":
#     t = Player('ass', True, ['Outside'], False)
