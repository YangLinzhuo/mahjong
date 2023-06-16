import copy

from yaku.hai import Hai, HaiType, Tehai
from yaku.mentsu import Mentsu, MentsuType, NakiType, ParsedMentsu


class YakuParser:
    def __init__(self):
        """
        :param input_tehai: current hold tehai
        :param input_hai:   current input hai
        """
        self.all_mentsu: set[ParsedMentsu] = set()
        self.has_head: bool = False

    def parse_mentsu(self, hai_seq: list[Hai], naki_type: NakiType):
        hai_seq = sorted(hai_seq)
        if naki_type == NakiType.NAKI:    # naki hai
            pass
        else:   # monzen hai
            cur_mentsu: list[Mentsu] = []
            self._parse_mongzen(hai_seq, 0, cur_mentsu)

    def is_shuntsu(self, hai1: Hai, hai2: Hai, hai3: Hai):
        if hai1.used or hai2.used or hai3.used:
            return False
        if (hai1.type == HaiType.YAKU) or (hai2.type == HaiType.YAKU) or (hai3.type == HaiType.YAKU):
            return False
        if (hai1.type != hai2.type) or (hai2.type != hai3.type) or (hai1.type != hai3.type):
            return False
        if (hai1.val + 1 == hai2.val) and (hai2.val + 1 == hai3.val):
            return True
        return False

    def is_kotsu(self, hai1: Hai, hai2: Hai, hai3: Hai):
        if hai1.used or hai2.used or hai3.used:
            return False
        if (hai1.type != hai2.type) or (hai2.type != hai3.type) or (hai1.type != hai3.type):
            return False
        if (hai1.val == hai2.val) and (hai2.val == hai3.val):
            return True
        return False

    def is_head(self, hai1: Hai, hai2: Hai):
        if hai1.used or hai2.used:
            return False
        if hai1.type != hai2.type:
            return False
        if hai1.val == hai2.val:
            return True
        return False

    def _parse_mongzen(self, hai_seq: list[Hai], start_idx: int, cur_mentsu: list[Mentsu]):
        i = start_idx
        if i >= len(hai_seq):
            self.all_mentsu.add(ParsedMentsu(copy.deepcopy(cur_mentsu)))
            return
        if hai_seq[i].used:
            self._parse_mongzen(hai_seq, i + 1, cur_mentsu)
        if i + 1 < len(hai_seq) and not self.has_head and self.is_head(hai_seq[i], hai_seq[i + 1]):
            cur_mentsu.append(Mentsu([hai_seq[i], hai_seq[i + 1]], MentsuType.HEAD, NakiType.MONGZEN))
            self.has_head = True
            hai_seq[i].used = True
            hai_seq[i + 1].used = True
            self._parse_mongzen(hai_seq, i + 2, cur_mentsu)
            cur_mentsu.pop()
            hai_seq[i].used = False
            hai_seq[i + 1].used = False
            self.has_head = False
        if i + 2 < len(hai_seq) and self.is_kotsu(hai_seq[i], hai_seq[i + 1], hai_seq[i + 2]):
            cur_mentsu.append(Mentsu([hai_seq[i], hai_seq[i + 1], hai_seq[i + 2]], MentsuType.KOTSU, NakiType.MONGZEN))
            hai_seq[i].used = True
            hai_seq[i + 1].used = True
            hai_seq[i + 2].used = True
            self._parse_mongzen(hai_seq, i + 3, cur_mentsu)
            hai_seq[i].used = False
            hai_seq[i + 1].used = False
            hai_seq[i + 2].used = False
            cur_mentsu.pop()
        for j in range(i + 1, min(len(hai_seq), i + 5)):
            for k in range(j + 1, min(len(hai_seq), j + 5)):
                if self.is_shuntsu(hai_seq[i], hai_seq[j], hai_seq[k]):
                    cur_mentsu.append(Mentsu([hai_seq[i], hai_seq[j], hai_seq[k]], MentsuType.SHUNTSU, NakiType.MONGZEN))
                    hai_seq[i].used = True
                    hai_seq[j].used = True
                    hai_seq[k].used = True
                    self._parse_mongzen(hai_seq, i + 1, cur_mentsu)
                    cur_mentsu.pop()
                    hai_seq[i].used = False
                    hai_seq[j].used = False
                    hai_seq[k].used = False

    def display(self):
        for mentsu in self.all_mentsu:
            print(mentsu)
