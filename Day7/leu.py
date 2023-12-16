from collections import Counter
from sys import argv

"""
     A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3,2
           RULE         HAND                                  WORTH
    Five of a kind   -> AAAAA [X,5]                         | => 100
    Four of a kind,  -> AA8AA [X,4][Y,1]                    | => 90
    Full house,      -> 23332 [X,3][Y,2]                    | => 80
    Three of a kind, -> TTT98 [X,3][Y,1][Z,1]               | => 70
    Two pair,        -> 23432 [X,2][Y,2][Z,1]               | => 60
    One pair,        -> A23A4 [X,2][Y,1][Z,1][N,1]          | => 50
    High card,       -> 23456 [X,1][Y,1][Z,1][N,1][M,1]     | => 40
    HIGH RULE:-

"""


class Card:
    _HIGH_RULE = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.bid = bid
        self.worth = self.calc_worth()
        self.dic = Counter(self.hand)

    def calc_worth(self):
        counts = Counter(self.hand)
        length = len(counts)
        _worth = 0
        # this one line and miss readig caued the mess
        if length == 1:
            _worth += 100
        elif length == 2:
            _worth += 80
            if counts.most_common(1)[0][1] == 4:
                _worth += 10
        elif length == 3:
            _worth += 60
            if counts.most_common(1)[0][1] == 3:
                _worth += 10
        elif length == 4:
            _worth += 50
        else:
            _worth += 40
        return _worth

    def __eq__(self, other: "Card") -> bool:
        return self.worth == other.worth

    def __lt__(self, other):
        if self != other:
            return self.worth < other.worth
        else:
            for x, y in zip(self.hand, other.hand):
                if x == y:
                    continue
                if Card._HIGH_RULE.index(x) < Card._HIGH_RULE.index(y):
                    return False
                else:
                    return True
            return True

    def __le__(self, other):
        return self.worth <= other.worth

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.hand} {self.bid} |=> {self.worth} , |=> {self.dic}"


def stroe_sorted(lis):
    with open(f"{argv[1]}_sorted", "w") as fp:
        for m in lis:
            fp.write(str(m) + "\n")


def main():
    ordered = [0] * 1000
    unordered = []
    with open(argv[1], "r") as fp:
        for n, i in enumerate(fp.readlines()):
            bid: int = int(i.strip().split(" ")[-1])
            hand: str = i.split(" ")[0]
            unordered.append(Card(hand=hand, bid=bid))

    ordered = sorted(unordered)
    stroe_sorted(ordered)
    print(sum(map(lambda x: (x[0] + 1) * x[1].bid, enumerate(ordered))))


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()