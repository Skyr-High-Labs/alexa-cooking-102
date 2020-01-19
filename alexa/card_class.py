import datetime
import math


class card:
    cards = []
    last_card = None
    answered = True
    time = datetime.date.today()

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.time = card.time
        self.repetitions = 0
        self.interval = 1
        self.easiness = 2.5
        card.cards.append([self.time, self])

    @staticmethod
    def print_test():
        chosens = card.cards
        for chosen in chosens:
            print([chosen[0], chosen[1].question])

    @staticmethod
    def draw_card():
        if not card.answered:
            card.cards.append([card.last_card.next_time, card.last_card])
        card.cards.sort(key=lambda c: c[0])
        if card.cards[0][0] <= card.time:
            last_card = card.cards.pop(0)[1]
            card.last_card = last_card
            card.answered = False
            return last_card.question
        return "No cards today!"

    @staticmethod
    def any_questions_left():
        card.cards.sort(key=lambda c: c[0])
        return (card.cards[0][0] <= card.time)

    @staticmethod
    def move_date(difference):
        card.time = card.time + datetime.timedelta(days=difference)

    @staticmethod
    def next_date():
        return card.last_card.time.strftime("%d/%m/%Y")

    @staticmethod
    def check_answer(answer):
        return card.last_card.answer == answer

    @staticmethod
    def return_card(quality):
        # called via set_score
        card.last_card.easiness = max(
            1.3, card.last_card.easiness + 0.1 - (5.0 - quality) * (0.08 + (5.0 - quality) * 0.02))
        if quality < 3:
            card.last_card.repetitions = 0
        else:
            card.last_card.repetitions += 1
        if card.last_card.repetitions <= 1:
            card.last_card.interval = 1
        elif card.last_card.repetitions == 2:
            card.last_card.interval = 6
        else:
            card.last_card.interval = math.ceil(
                card.last_card.interval*card.last_card.easiness)
        card.last_card.time = card.last_card.next_time
        card.answered = True
        card.cards.append([card.last_card.next_time, card.last_card])
        card.cards.sort(key=lambda c: c[0])

    @staticmethod
    def get_correct_answer():
        return card.last_card.answer

    def next_time(self):
        return self.time + datetime.timedelta(days=math.ceil(self.interval))

    def get_current_date():
        return card.time.strftime("%d/%m/%Y")
    next_time = property(next_time)
