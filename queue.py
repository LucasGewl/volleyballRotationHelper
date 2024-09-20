from typing import Any


class Queue:
    _items: list[Any]

    def __init__(self, items: list[Any]):
        self._items = items[:]

    def enqueue(self, item: Any) -> None:
        self._items.insert(0, item)

    def dequeue(self) -> Any:
        return self._items.pop()

    def shift_back(self) -> None:
        self._append(None)

        for i in range(4, -1, -1):
            self._items[i + 1] = self._items[i]

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __setitem__(self, index: int, val: Any) -> None:
        self._items[index] = val

    def __eq__(self, other):
        if len(self._items) != len(other._items):
            return False

        else:
            for i in range(len(self._items)):
                if self[i] != other[i]:
                    return False
            return True

    def _append(self, item) -> None:
        self._items.append(item)



if __name__ == "__main__":
    q = Queue([1, 2, 3])
    print(q[0])
