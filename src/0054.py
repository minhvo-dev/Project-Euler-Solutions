class Card():
    def __init__(self, s: str):
        if(s[0] == 'T'):
            self._value = 10
        elif(s[0] == 'J'):
            self._value = 11
        elif(s[0] == 'Q'):
            self._value = 12
        elif(s[0] == 'K'):
            self._value = 13
        elif(s[0] == 'A'):
            self._value = 14
        else:
            self._value = int(s[0])
        self._suit = s[1]

    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit


class Hand():
    def __init__(self, cards: list):
        self._cards = [Card(c) for c in cards]
        self._cards.sort(key=lambda card: card.value)
        self._valueArr = [[] for _ in range(15)]
        self._suitArr = [[] for _ in range(4)]  # C, D, H, S
        for c in self._cards:
            self._valueArr[c.value].append(c)
            if(c.suit == 'C'):
                self._suitArr[0].append(c)
            elif(c.suit == 'D'):
                self._suitArr[1].append(c)
            elif(c.suit == 'H'):
                self._suitArr[2].append(c)
            else:
                self._suitArr[3].append(c)

    def get_nth_highest_value_card(self, n: int):
        count = 0
        for i in range(14, 2, -1):
            if(len(self._valueArr[i]) > 0):
                count += 1
                if(count == n):
                    return self._valueArr[i][0].value
        return -1

    def is_royal_flush(self):
        for suit in self._suitArr:
            if(len(suit) == 5 and sum([c.value for c in suit]) == 60):
                return True
        return False

    def is_straight_flush(self):
        for suit in self._suitArr:
            if(len(suit) == 5):
                for i in range(1, 5):
                    if(suit[i].value - suit[i - 1].value != 1):
                        return -1
                return self._cards[4].value
        return -1

    def is_four_of_a_kind(self):
        for value in self._valueArr:
            if(len(value) == 4):
                return value[0].value
        return -1

    def is_full_house(self):
        # cards on hand are sorted
        if(self._cards[0].value == self._cards[1].value):
            # pair or triplet
            if(self._cards[0].value == self._cards[2].value):
                # triplet
                if(self._cards[3].value == self._cards[4].value):
                    return [self._cards[0].value, self._cards[3].value]
            else:
                # pair
                if(self._cards[2].value == self._cards[3].value and self._cards[2].value == self._cards[4].value):
                    return [self._cards[2].value, self._cards[0].value]
        return -1

    def is_flush(self):
        for suit in self._suitArr:
            if(len(suit) == 5):
                return self._cards[4].value
        return -1

    def is_straight(self):
        for i in range(1, 5):
            if(self._cards[i].value - self._cards[i - 1].value != 1):
                return -1
        return self._cards[4].value

    def is_three_of_a_kind(self):
        for value in self._valueArr:
            if(len(value) == 3):
                return value[0].value
        return -1

    def is_two_pairs(self):
        if(self._cards[0].value == self._cards[1].value):
            if(self._cards[2].value == self._cards[3].value):
                return [self._cards[0].value, self._cards[2].value, self._cards[4].value]
            if(self._cards[3].value == self._cards[4].value):
                return [self._cards[0].value, self._cards[3].value, self._cards[2].value]
            return -1
        elif(self._cards[1].value == self._cards[2].value and self._cards[3].value == self._cards[4].value):
            return [self._cards[1].value, self._cards[3].value, self._cards[0].value]
        return -1

    def is_a_pair(self):
        p = -1
        for value in self._valueArr:
            if(len(value) == 2):
                p = value[0].value
        if(p == -1):
            return -1
        res = [p]
        for c in self._cards[::-1]:
            if(c.value != p):
                res.append(c.value)
        return res


def process_a_game(s: str):
    """process a poker game

    Args:
        s (str): 10 cards

    Returns:
        [int]: 0 if due, 1 if player 1 win, 2 if player 2 win
    """
    cards = s.split(" ")
    h1 = Hand(cards[:5])
    h2 = Hand(cards[5:])
    # check for royal flush
    v1 = h1.is_royal_flush()
    v2 = h2.is_royal_flush()
    if(v1 == True and v2 == True):
        return 0
    if(v1 == True):
        return 1
    if(v2 == True):
        return 2
    # check for strait flush
    v1 = h1.is_straight_flush()
    v2 = h2.is_straight_flush()
    if(v1 != -1 and v2 != -1):
        if(v1 > v2):
            return 1
        if(v2 > v1):
            return 2
        return 0
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for four of a kind
    v1 = h1.is_four_of_a_kind()
    v2 = h2.is_four_of_a_kind()
    if(v1 != -1 and v2 != -1):
        if(v1 > v2):
            return 1
        return 2
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for full house
    v1 = h1.is_full_house()
    v2 = h2.is_full_house()
    if(v1 != -1 and v2 != -1):
        if(v1[0] > v2[0]):
            return 1
        return 2
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for flush
    v1 = h1.is_flush()
    v2 = h2.is_flush()
    if(v1 != -1 and v2 != -1):
        if(v1 == v2):
            for i in range(2, 6):
                v1 = h1.get_nth_highest_value_card(i)
                v2 = h2.get_nth_highest_value_card(i)
                if(v1 > v2):
                    return 1
                if(v2 > v2):
                    return 2
            return 0
        if(v1 > v2):
            return 1
        return v2
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for straight
    v1 = h1.is_straight()
    v2 = h2.is_straight()
    if(v1 != -1 and v2 != -1):
        if(v1 == v2):
            return 0
        if(v1 > v2):
            return 1
        return 2
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for three of a kind
    v1 = h1.is_three_of_a_kind()
    v2 = h2.is_three_of_a_kind()
    if(v1 != -1 and v2 != -1):
        if(v1 > v2):
            return 1
        return 2
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for two pairs
    v1 = h1.is_two_pairs()
    v2 = h2.is_two_pairs()
    if(v1 != -1 and v2 != -1):
        if(v1[1] == v2[1]):
            if(v1[2] > v2[2]):
                return 1
            if(v2[2] > v1[2]):
                return 2
            return 0
        if(v1[1] > v2[1]):
            return 1
        return 2
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for a pair
    v1 = h1.is_a_pair()
    v2 = h2.is_a_pair()
    if(v1 != -1 and v2 != -1):
        if(v1[0] == v2[0]):
            for i in range(1, 4):
                if(v1[i] > v2[i]):
                    return 1
                if(v2[i] > v1[i]):
                    return 2
            return 0
        if(v1[0] > v2[0]):
            return 1
        return 2
    if(v1 != -1):
        return 1
    if(v2 != -1):
        return 2
    # check for highest card
    for i in range(1, 6):
        v1 = h1.get_nth_highest_value_card(i)
        v2 = h2.get_nth_highest_value_card(i)
        if(v1 > v2):
            return 1
        if(v2 > v1):
            return 2
    return 0


def read_cards_from_file(path: str):
    f = open(path, "r")
    cards = f.read()
    f.close()
    return cards.split("\n")[:-1]  # remove the last empty line


def no_math_solution():
    path = "./data/p054_poker.txt"
    count = 0
    for c in read_cards_from_file(path):
        if(process_a_game(c) == 1):
            count += 1
    return count


if __name__ == "__main__":
    print(no_math_solution())
