from enum import Enum
from yaku.hai import Hai


class MentsuType(Enum):
    SHUNTSU = 0
    KOTSU = 1
    KANGTSU = 2


class NakiType(Enum):
    """
        Whether this mentsu is nakihai or not
    """
    NAKI = 0
    MONGZEN = 1


class Mentsu:
    def __init__(self, hai_seq: list[Hai], mentsu_type: MentsuType, naki_type: NakiType):
        self.mentsu_type = mentsu_type
        self.naki_type = naki_type
        self.hai_seq: list[Hai] = hai_seq
