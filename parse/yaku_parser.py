from yaku.hai import Hai, HaiType, Tehai
from yaku.mentsu import Mentsu, MentsuType, NakiType


class YakuParser:
    def __init__(self, input_tehai: Tehai, input_hai: Hai):
        """
        :param input_tehai: current hold tehai
        :param input_hai:   current input hai
        """
        self.tehai = input_tehai
        self.input_hai = input_hai
        self.all_mentsu: list[list[Mentsu]] = []

    def parse_mentsu(self, hai_seq: list[Hai], naki_type: NakiType):
        mentsu_lst: list[Mentsu] = []
        sorted(hai_seq)
        if naki_type == NakiType.NAKI:    # naki hai
            pass
        else:   # monzen hai
            i = 0
            pass

    def is_shuntsu(self, hai1: Hai, hai2: Hai, hai3: Hai):
        if (hai1.type == HaiType.YAKU) or (hai2.type == HaiType.YAKU) or (hai3.type == HaiType.YAKU):
            return False
        if (hai1.type != hai2.type) or (hai2 != hai3.type) or (hai1.type != hai3):
            return False
        if (hai1.val + 1 == hai2.val) and (hai2.val + 1 == hai3.val):
            return True
        return False

    def is_kotsu(self, hai1: Hai, hai2: Hai, hai3: Hai):
        if (hai1.type != hai2.type) or (hai2 != hai3.type) or (hai1.type != hai3):
            return False
        if (hai1.val == hai2.val) and (hai2.val == hai3.val):
            return True
        return False

    def parse_mongzen(self, hai_seq: list[Hai], start_idx: int, cur_mentsu: list[Mentsu]):
        i = start_idx
        if i >= len(hai_seq):
            self.all_mentsu.append(cur_mentsu)
            return
        while i + 2 < len(hai_seq):
            if self.is_shuntsu(hai_seq[i], hai_seq[i + 1], hai_seq[i + 2]):
                cur_mentsu.append(Mentsu(hai_seq[i:i + 2], MentsuType.SHUNTSU, NakiType.MONGZEN))
                self.parse_mongzen(hai_seq, i + 3, cur_mentsu)
                cur_mentsu.pop()
            elif self.is_kotsu(hai_seq[i], hai_seq[i + 1], hai_seq[i + 2]):
                cur_mentsu.append(Mentsu(hai_seq[i:i + 2], MentsuType.KOTSU, NakiType.MONGZEN))
                self.parse_mongzen(hai_seq, i + 3, cur_mentsu)
                cur_mentsu.pop()
            else:
                pass
