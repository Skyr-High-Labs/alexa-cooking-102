# -*- coding: utf-8 -*-

"""Utility module to generate text for commonly used responses."""

import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type
import backend

from . import data


def get_random_state(states_list):
    """Return a random value from the list of states."""
    return random.choice(states_list)


def state_properties():
    """Return the list of state properties."""
    val = ["abbreviation", "capital", "statehood_year",
           "statehood_order"]
    return val


def get_random_state_property():
    """Return a random state property."""
    return random.choice(state_properties())


def get_card_description(item):
    """Return the description shown on card in Alexa response."""
    text = "State Name: {}\n".format(item['state'])
    text += "State Capital: {}\n".format(item['capital'])
    text += "Statehood Year: {}\n".format(item['statehood_year'])
    text += "Statehood Order: {}\n".format(item['statehood_order'])
    text += "Abbreviation: {}\n".format(item['abbreviation'])
    return text

def any_questions_left():
    return backend.any_questions_left()

def supports_display(handler_input):
    # type: (HandlerInput) -> bool
    """Check if display is supported by the skill."""
    try:
        if hasattr(
            handler_input.request_envelope.context.system.device.
                supported_interfaces, 'display'):
            return (
                handler_input.request_envelope.context.system.device.
                supported_interfaces.display is not None)
    except:
        return False


def get_bad_answer(item):
    """Return response text for incorrect answer."""
    return "{} {}".format(data.BAD_ANSWER.format(item), data.HELP_MESSAGE)


def get_current_score(score, counter):
    """Return the response text for current quiz score of the user."""
    return data.SCORE.format("current", score, counter)


def get_final_score(score, counter):
    """Return the response text for final quiz score of the user."""
    return data.SCORE.format("final", score, counter)


def get_card_title(item):
    """Return state name as card title."""
    return item["state"]


def get_image(ht, wd, label):
    """Get flag image with specified height, width and state abbr as label."""
    return data.IMG_PATH.format(str(ht), str(wd), label)


def get_small_image(item):
    """Get state flag small image (720x400)."""
    return get_image(720, 400, item['abbreviation'])


def get_large_image(item):
    """Get state flag large image (1200x800)."""
    return get_image(1200, 800, item['abbreviation'])


def get_speech_description(item):
    """Return state information in well formatted text."""
    return data.SPEECH_DESC.format(
        item['state'], item['statehood_order'], item['statehood_year'],
        item['state'], item['capital'], item['state'], item['abbreviation'],
        item['state'])


def get_ordinal_indicator(counter):
    """Return st, nd, rd, th ordinal indicators according to counter."""
    if counter == 1:
        return "1st"
    elif counter == 2:
        return "2nd"
    elif counter == 3:
        return "3rd"
    else:
        return "{}th".format(str(counter))


def __get_attr_for_speech(attr):
    """Helper function to convert attribute name."""
    return attr.lower().replace("_", " ").strip()


def get_question_without_ordinal(attr, item):
    return "What is the {} of {}. ".format(
        __get_attr_for_speech(attr), item["state"])


def get_question(counter, attr, item):
    """Return response text for nth question to the user."""
    return (
        "Here is your {} question. {}").format(
        get_ordinal_indicator(counter),
        get_question_without_ordinal(attr, item))


def get_answer():
    """Return response text for correct answer to the user."""
    
    return backend.get_answer()

# TODO: replace w peter's code
def is_answer_correct():
    # (HandlerInput) -> None
    return backend.get_question()
    


def get_speechcon(correct_answer):
    """Return speechcon corresponding to the boolean answer correctness."""
    text = ("<say-as interpret-as='interjection'>{} !"
            "</say-as><break strength='strong'/>")
    if correct_answer:
        return text.format(random.choice(data.CORRECT_SPEECHCONS))
    else:
        return text.format(random.choice(data.WRONG_SPEECHCONS))


def get_multiple_choice_answers(item, attr, states_list):
    """Return multiple choices for the display to show."""
    answers_list = [item[attr]]
    # Insert the correct answer first

    while len(answers_list) < 3:
        state = random.choice(states_list)

        if not state[attr] in answers_list:
            answers_list.append(state[attr])

    random.shuffle(answers_list)
    return answers_list


def get_item(slots, states_list):
    """Get matching data object from slot value."""
    item = []
    resolved_slot = None
    for _, slot in six.iteritems(slots):
        if slot.value is not None:
            resolved_slot = slot.value
            for state in states_list:
                for _, v in six.iteritems(state):
                    if v.lower() == slot.value.lower():
                        item.append(state)
            if len(item) > 0:
                return item[0], True
    else:
        return resolved_slot, False


def compare_token_or_slots(handler_input, value):
    """Compare value with slots or token,
        for display selected event or voice response for quiz answer."""
    return compare_slots(
        handler_input.request_envelope.request.intent.slots, value)


def compare_slots(slots, value):
    """Compare slot value to the value provided."""
    return slot.value.lower() == value.lower()
    
