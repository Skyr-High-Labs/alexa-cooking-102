# -*- coding: utf-8 -*-

"""Utility module to generate text for commonly used responses."""

import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type
import card as backend

from . import data

def any_questions_left():
    return backend.any_questions_left()



def get_question():
    # TODO: deal with the EOf thing
    return backend.draw_card()


def get_answer():
    """Return response text for correct answer to the user."""
    
    return backend.get_correct_answer()

def is_answer_correct(answer):
    # (HandlerInput) -> None
    # TODO: impleemnt percentage accuracy instead of one-one accuracy
    return backend.is_answer_correct(answer)
    
def set_score(score):
    backend.return_card(int(score))
    
def get_speechcon(correct_answer):
    """Return speechcon corresponding to the boolean answer correctness."""
    text = ("<say-as interpret-as='interjection'>{} !"
            "</say-as><break strength='strong'/>")
    if correct_answer:
        return text.format(random.choice(data.CORRECT_SPEECHCONS))
    else:
        return text.format(random.choice(data.WRONG_SPEECHCONS))

