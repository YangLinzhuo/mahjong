from yaku.hai import Tehai
from yaku.mentsu import NakiType
from parse.yaku_parser import YakuParser


def main():
    # input_str = "11123456678999m"
    input_str = "12312312345677m"
    tehai = Tehai()
    tehai.parse_input(input_str)
    parser = YakuParser()
    parser.parse_mentsu(tehai.mongzen, NakiType.MONGZEN)
    parser.display()


if __name__ == '__main__':
    main()
