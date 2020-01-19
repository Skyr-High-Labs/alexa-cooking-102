# -*- coding: utf-8 -*-

"""Utility module to generate text for commonly used responses."""
import random
import alexa.card_class as backend

import alexa.data as data

def test():
    backend.card.print_test()

def any_questions_left():
    return backend.card.any_questions_left()


def get_question():
    # TODO: deal with the EOf thing
    return backend.card.draw_card()


def get_answer():
    """Return response text for correct answer to the user."""
    return backend.card.get_correct_answer()


def is_answer_correct(answer):
    # (HandlerInput) -> None
    # TODO: impleemnt percentage accuracy instead of one-one accuracy
    return backend.card.check_answer(answer)


def set_score(score):
    backend.card.return_card(int(score))


def get_speechcon(correct_answer):
    """Return speechcon corresponding to the boolean answer correctness."""
    text = ("<say-as interpret-as='interjection'>{} !"
            "</say-as><break strength='strong'/>")
    if correct_answer:
        return text.format(random.choice(data.CORRECT_SPEECHCONS))
    else:
        return text.format(random.choice(data.WRONG_SPEECHCONS))

def move_date(diff):
    backend.card.move_date(diff)

def next_date():
    return(backend.card.next_date())

def get_current_date():
    return (backend.card.get_current_date())
