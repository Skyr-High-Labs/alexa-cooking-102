# -*- coding: utf-8 -*-

SKILL_TITLE = "Prep Me"

WELCOME_MESSAGE = ("Welcome to Prep Me. Are you ready to revise?")

START_QUIZ_MESSAGE = ("Great, let's begin!")

END_QUIZ_MESSAGE = ("No more questions today!")

SCORE_ANSWER_MESSAGE = (
    "On a scale of one to three, how easy did you find this question?")
EXIT_SKILL_MESSAGE = ("Stopping your revision now!")

REPROMPT_SPEECH = "Sorry, I didn't hear that."

HELP_MESSAGE = ("This is a Spaced Repetition App. I will help you revise your flash cards.")

CORRECT_SPEECHCONS = ['Bingo',
                      'Boom', 'Bravo', 'Cha Ching', 'Cheers', 'Dynomite',
                      'Hip hip hooray', 'Hurrah', 'Hurray', 'Huzzah',
                      'Oh dear.  Just kidding.  Hurray', 'Kaboom', 'Kaching',
                      'Oh snap', 'Phew', 'Righto', 'Way to go', 'Well done',
                      'Whee', 'Woo hoo', 'Yay', 'Wowza', 'Yowsa']

WRONG_SPEECHCONS = ['Argh', 'Aw man', 'Blarg', 'Blast', 'Boo', 'Bummer',
                    'Darn', "D'oh", 'Dun dun dun', 'Eek', 'Honk', 'Le sigh',
                    'Mamma mia', 'Oh boy', 'Oh dear', 'Oof', 'Ouch', 'Ruh roh',
                    'Shucks', 'Uh oh', 'Wah wah', 'Whoops a daisy', 'Yikes']

IMG_PATH = (
    "https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/"
    "alexa-skills-kit/tutorials/quiz-game/state_flag/{}x{}/{}._TTH_.png")

USE_CARDS_FLAG = True

MAX_QUESTIONS = 10

BAD_ANSWER = (
    "I'm sorry. {} is not something I know very much about in this skill.")

FALLBACK_ANSWER = (
    "Sorry. I can't help you with that. {}".format(HELP_MESSAGE))

SCORE = "Your {} score is {} out of {}. "

SPEECH_DESC = (
    "{} is the {} state, "
    "admitted to the Union in {}.  "
    "The capital of {} is {}, and the "
    "abbreviation for {} is "
    "<break strength='strong'/><say-as interpret-as='spell-out'>"
    "{}</say-as>.  I've added {} to "
    "your Alexa app.  Which other state or capital would you like to "
    "know about? ")
