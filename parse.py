import copy
import pprint
import re

all_mentsu = []
HEAD = False

def is_shuntsu(seq: list[str]):
    if len(seq) != 3:
        return False
    if seq[0][1] == 'z' or seq[1][1] == 'z' or seq[2][1] == 'z':
        return False
    if seq[0][1] != seq[1][1] or seq[1][1] != seq[2][1] or seq[0][1] != seq[2][1]:
        return False
    if int(seq[0][0]) + 1 == int(seq[1][0]) and int(seq[1][0]) + 1 == int(seq[2][0]):
        return True
    return False


def is_kotsu(seq: list[str]):
    if len(seq) != 3:
        return False
    if seq[0][1] != seq[1][1] or seq[1][1] != seq[2][1] or seq[0][1] != seq[2][1]:
        return False
    if seq[0][0] == seq[1][0] and seq[1][0] == seq[2][0]:
        return True
    return False


def is_head(seq: list[str]):
    if len(seq) != 2:
        return False
    if seq[0][1] != seq[1][1]:
        return False
    if seq[0][0] == seq[1][0]:
        return True
    return False

def parse(tehai: list[str], start_idx: int, cur_mentsu: list[list[str]]):
    global HEAD
    i = start_idx
    if i >= len(tehai):
        all_mentsu.append(copy.deepcopy(cur_mentsu))
        return
    if not HEAD and is_head(tehai[i: i + 2]):
        cur_mentsu.append(tehai[i:i + 2])
        HEAD = True
        parse(tehai, i + 2, cur_mentsu)
        cur_mentsu.pop()
        HEAD = False
    if is_kotsu(tehai[i:i + 3]):
        cur_mentsu.append(tehai[i:i + 3])
        parse(tehai, i + 3, cur_mentsu)
        cur_mentsu.pop()
    for j in range(i + 1, min(len(tehai), i + 5)):
        for k in range(j + 1, min(len(tehai), j + 5)):
            if is_shuntsu([tehai[i], tehai[j], tehai[k]]):
                cur_mentsu.append([tehai[i], tehai[j], tehai[k]])
                parse(tehai, i + 3, cur_mentsu)
                cur_mentsu.pop()


if __name__ == "__main__":
    inputs = "1m1m2m2m3m3m7m8m9m1s2s3s9p9p"
    cur_mentsu = []
    parse(re.findall('..', inputs), 0, cur_mentsu)
    pprint.pprint(all_mentsu)
