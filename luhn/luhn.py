class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(' ', '')
        self.card_num = card_num

    def valid(self):
        card_num = [x for x in self.card_num]
        
        if len(card_num) <= 1:
            return False

        for i, num in enumerate(card_num):
            if not str(num).isdigit():
                return False
            card_num[i] = int(num)

        for i in range(len(card_num) - 2, -1, -2):
            card_num[i] = card_num[i] * 2
            if card_num[i] > 9:
                card_num[i] -= 9

        return sum(card_num) % 10 == 0

