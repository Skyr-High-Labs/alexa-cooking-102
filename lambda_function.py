# -*- coding: utf-8 -*-


import json

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.serialize import DefaultSerializer
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractResponseInterceptor, AbstractRequestInterceptor)
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_core.response_helper import (
    get_plain_text_content, get_rich_text_content)

from ask_sdk_model.interfaces.display import (
    ImageInstance, Image, RenderTemplateDirective, ListTemplate1,
    BackButtonBehavior, ListItem, BodyTemplate2, BodyTemplate1)
from ask_sdk_model import ui, Response

from alexa import data, util


# Skill Builder object
sb = SkillBuilder()

last_speech = ""


# Request Handler classes
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        last_speech = ""
        handler_input.response_builder.speak(data.WELCOME_MESSAGE).ask(
            data.HELP_MESSAGE)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for skill session end."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        last_speech = ""
        print("Session ended with reason: {}".format(
            handler_input.request_envelope))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for help intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        handler_input.attributes_manager.session_attributes = {}
        # Resetting session

        handler_input.response_builder.speak(
            data.HELP_MESSAGE).ask(data.HELP_MESSAGE)
        return handler_input.response_builder.response


class ExitIntentHandler(AbstractRequestHandler):
    """Single Handler for Cancel, Stop and Pause intents."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input) or
                is_intent_name("AMAZON.PauseIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        handler_input.response_builder.speak(
            data.EXIT_SKILL_MESSAGE).set_should_end_session(True)
        return handler_input.response_builder.response


class RevisionHandler(AbstractRequestHandler):
    """Handler for starting a revision.

    The ``handle`` method will initiate a revision state and build a
    question from the states data, using the util methods.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name( RevisionIntent")(handler_input) or
                is_intent_name("AMAZON.StartOverIntent")(handler_input))

    def handle(self, handler_input):
        question = util.get_question()
        speech = question
        response_builder = handler_input.response_builder
        response_builder.speak(speech)
        response_builder.ask(speech)
        # backup last speech
        last_speech = speech
        return response_builder.response

    
class RevisionAnswerHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AnswerIntent")(handler_input) )

    def handle(self, handler_input):
        response_builder = handler_input.response_builder 

        if util.is_answer_correct(handler_input.request_envelope.request.intent.slots["answer"]):
            speech = util.get_speechcon(correct_answer=True)
            # rating
            speech += data.SCORE_ANSWER_MESSAGE
            reprompt = data.SCORE_ANSWER_MESSAGE
            # backup last speech
            last_speech = speech
            return response_builder.speak(speech).ask(reprompt).response
        else:
            speech = util.get_speechcon(correct_answer=False)
            speech += "The correct answer is " + util.get_answer()
            if util.any_questions_left():
                # Ask another question
                question = util.get_question()
                speech += question
                reprompt = question
                # backup last speech
                last_speech = speech
                return response_builder.speak(speech).ask(reprompt).response
            else:
                speech += data.END_QUIZ_MESSAGE + data.EXIT_SKILL_MESSAGE
                response_builder.set_should_end_session(True)
                # backup last speech
                last_speech = speech
                return response_builder.speak(speech).response


class RevisionAnswerScoreHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AnswerScoreIntent")(handler_input))

    def handle(self, handler_input):

        response_builder = handler_input.response_builder

        util.set_score(
            handler_input.request_envelope.request.intent.slots["score"])

        if util.any_questions_left():
            # ask next question
            question = util.get_question()
            speech = question
            reprompt = question
            # backup last speech
            last_speech = speech
            return response_builder.speak(speech).ask(reprompt).response
        else:
            # finished all messages, quit session
            speech = data.END_QUIZ_MESSAGE + data.EXIT_SKILL_MESSAGE
            response_builder.set_should_end_session(True)
            # backup last speech
            last_speech = speech
            return response_builder.speak(speech).response

class RepeatHandler(AbstractRequestHandler):
    """Handler for repeating the response to the user."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        response_builder = handler_input.response_builder
        if last_speech:
            speech = last_speech
            return response_builder.speak(speech).response
        else:
            return response_builder.speak(data.FALLBACK_ANSWER).ask(data.HELP_MESSAGE).response

# Exception Handler classes
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch All Exception handler.
    This handler catches all kinds of exceptions and prints
    the stack trace on AWS Cloudwatch with the request envelope."""
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        speech = "Sorry, there was some problem. Please try again!!"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response





# Add all request handlers to the skill.
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(RevisionHandler())
sb.add_request_handler(RevisionAnswerHandler())
sb.add_request_handler(RepeatHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(ExitIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Add exception handler to the skill.
sb.add_exception_handler(CatchAllExceptionHandler())

# Add response interceptor to the skill.
# sb.add_global_response_interceptor(CacheResponseForRepeatInterceptor())


# Expose the lambda handler to register in AWS Lambda.
lambda_handler = sb.lambda_handler()
