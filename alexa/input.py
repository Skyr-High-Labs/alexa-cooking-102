import json
from alexa.card import card


def read_data():
    with open('sample.json') as json_file:
        data = json.load(json_file)
    for i in range(len(data[0])):
        card(data[i]["question"], data[i]["answer"])
    print(card.cards[0].question)
    print(card.cards[0].answer)


class InputReader:
    if __name__ == '__main__':
        read_data()
