from enum import Enum


class HaiType(Enum):
    MANTSU = 'm'  # man -> m
    PINTSU = 'p'  # pin -> p
    SOUTSU = 's'  # sou -> s
    YAKU = 'z'   # yaku -> z


HAITYPE_MAP = {
    'm': HaiType.MANTSU,
    'p': HaiType.PINTSU,
    's': HaiType.SOUTSU,
    'z': HaiType.YAKU
}


class Hai:
    """
        This is a class of Hai(mahjong hai), which records information
        about one mahjong hai.
    """
    def __init__(self, hai_type: HaiType, val: int):
        """
            :param hai_type: type of this hai, totally 4 types, m, p, s, z
            :param val: the value of this hai, 1~9 for m, p, s, and 1~7 stands for 東南西北白發中
        """
        self.type: HaiType = hai_type
        self.val: int = val
        self.used: bool = False

    def __lt__(self, other):
        return (self.type.value < other.type.value) or (self.type == other.type and self.val < other.val)

    def __gt__(self, other):
        return (self.type.value > other.type.value) or (self.type == other.type and self.val > other.val)

    def __eq__(self, other):
        return self.type == other.type and self.val == other.val

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


class Tehai:
    """
        Class of current tehai
    """
    def __init__(self):
        self.mongzen: list[Hai] = []    # initially 13 hai
        self.naki: list[Hai] = []       # initially 0

    def parse_input(self, tehai: str):
        from collections import deque
        stack = deque()
        for c in tehai:
            if c.isnumeric():
                stack.append(int(c))
            else:
                while len(stack):
                    val = stack.pop()
                    self.mongzen.append(Hai(HAITYPE_MAP[c], val))
