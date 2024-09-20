from player import Player
from queue import Queue


class Rotation:
    """
    The rotation decided before the game

    === Public Attributes ===
    players: the players in the rotation
    onCourt: The players on the court, onCourt[0] means in 6, onCourt[5] means in
    Service
    offCourt: The players off the court, sorted by which positions they are.
    offCourt[position][0] means they are the last in the queue to get on.

    === Representation Invariants ===
    - len(onCourt) == 6
    - All players must have <currentPosition> set BEFORE a rotation is made
    """
    players: list[Player]
    # onCourt is a Queue
    onCourt = Queue[Player]
    # offCourt is a Queue
    offCourt = dict[str, Queue[Player]]

    def __init__(self, onCourt: list[Player], offCourt: dict[list[Player]]):
        self.onCourt = Queue(onCourt[:])
        self.offCourt = {}
        self.players = onCourt[:]
        for key in offCourt.keys():
            self.offCourt[key] = Queue(offCourt[key][:])
            self.players.extend(offCourt[key][:])


    def rotate(self) -> None:
        leavingCourt = self.onCourt.dequeue()

        self.onCourt.shift_back()

        # find next player to go in
        offCourtPositions = self.offCourt.keys()

        if leavingCourt.currentPosition in offCourtPositions:
            currentPositions = self.offCourt[leavingCourt.currentPosition]
            currentPositions.enqueue(leavingCourt)
            nextIn = currentPositions.dequeue()
        else:
            nextIn = leavingCourt

        self.onCourt[0] = nextIn

    def __eq__(self, other) -> bool:
        # todo: replace onCourt and offCourt with Queues with implemented
        # todo: __eq__ functions since lists are equal even with wrong order
        if self.onCourt == other.onCourt and self.offCourt == other.offCourt:
            return True
        else:
            return False

if __name__ == "__main__":
    p1 = Player('a', True, ['Opposite'], False)
    p2 = Player('b', True, ['Opposite'], False)
    p3 = Player('c', True, ['Opposite'], False)
    p4 = Player('d', True, ['Opposite'], False)
    p5 = Player('e', True, ['Opposite'], False)
    p6 = Player('f', True, ['Opposite'], False)
    p7 = Player('g', True, ['Opposite'], False)

    p1.setPosition('Opposite')
    p2.setPosition('Opposite')
    p3.setPosition('Opposite')
    p4.setPosition('Opposite')
    p5.setPosition('Opposite')
    p6.setPosition('Opposite')
    p7.setPosition('Opposite')

    r1 = Rotation([p1, p2, p3, p4, p5, p6], {'Opposite': [p7]})
    r2 = Rotation([p1, p2, p3, p4, p5, p6], {'Opposite': [p7]})

    print(r1 == r2)
    print(r1.onCourt)
    print(r1.offCourt)

    r1.rotate()
    print(r1 == r2)



