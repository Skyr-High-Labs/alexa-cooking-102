import json
from alexa.card import card


def read_data(input_name):
    with open(input_name) as json_file:
        data = json.load(json_file)
    for i in range(len(data[0])):
        card(data[i]["question"], data[i]["answer"])


class InputReader:
    if __name__ == '__main__':
        read_data('sample.json')
