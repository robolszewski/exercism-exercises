def response(hey_bob):

    import random

    
    random_number:int = randint(0,4)
    BOBS_RESPONSES:tuple = ("Sure", "Whoa, chill out!", "Calm down, I know what I'm doing!", "Fine. Be that way!", "Whatever")

    return BOBS_RESPONSES[random_number]
