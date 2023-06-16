from enum import Enum
from yaku.hai import Hai, HaiType, HAITYPE_MAP


class MentsuType(Enum):
    SHUNTSU = 0
    KOTSU = 1
    KANGTSU = 2
    HEAD = 3


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

    def __repr__(self):
        if len(self.hai_seq) == 0:
            return ""
        val = "".join([str(hai.val) for hai in self.hai_seq])
        return f"{val}{self.hai_seq[0].type.value}"


class ParsedMentsu:
    def __init__(self, parsed_mentsu: list[Mentsu]):
        self.parsed_mentsu = parsed_mentsu

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return "".join(str(mentsu) for mentsu in self.parsed_mentsu)

    def __eq__(self, other):
        return hash(self) == hash(other)
