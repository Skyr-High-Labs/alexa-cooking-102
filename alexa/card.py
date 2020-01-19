import datetime
import heapq
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
        card.cards.append(self)

    @staticmethod
    def draw_card():
        if not card.answered:
            heapq.heappush(card.cards, [card.last_card.next_time, card.last_card])
        if card.cards[0][1].next_time > card.time:
            return "EOF, users shouldn't see this"
        last_card = heapq.heappop(card.cards)[1]
        card.answered = False
        return last_card.question

    @staticmethod
    def check_queue():
        if card.cards[0][1].next_time > card.time:
            return False
        else:
            return True

    @staticmethod
    def move_date(difference):
        card.time = card.time + datetime.timedelta(days=difference)

    @staticmethod
    def next_date():
        return card.last_card.next_time.strftime("%d/%m/%Y")

    @staticmethod
    def check_answer(last_card, answer):
        return last_card.answer == answer

    @staticmethod
    def return_card(quality):
        card.last_card.easiness = max(1.3, card.last_card.easiness + 0.1 - (5.0 - quality) * (0.08 + (5.0 - quality) * 0.02))
        if quality < 3:
            card.last_card.repetitions = 0
        else:
            card.last_card.repetitions += 1
        if card.last_card.repetitions == 1:
            card.last_card.interval = 1
        elif card.last_card.repetitions == 2:
            card.last_card.interval = 6
        else:
            card.last_card.interval *= card.last_card.easiness
        card.last_card.time = card.time
        card.answered = True
        heapq.heappush(card.cards, [card.last_card.next_time, card.last_card])

    @staticmethod
    def right_answer():
        return card.last_card.answer

    def next_time(self):
        return self.time + datetime.timedelta(days=math.ceil(self.interval))

    next_time = property(next_time)
