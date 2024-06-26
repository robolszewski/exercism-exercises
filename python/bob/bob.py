def response(hey_bob):
    """Instructions

Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

Bob only ever answers one of five things:

    "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    "Whatever." This is what he answers to anything else.

"""
    #strip spaces from string
    hey_bob = hey_bob.strip()

    #check to see if response is blank
    if hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!";

    #Check to see if a question is being YELLED at Bob
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"; 
    
    #Check to see if Bob is being yelled at
    if hey_bob.isupper(): 
        return "Whoa, chill out!"
    
    #Check to see if a question is being asked of Bob
    if hey_bob[-1] == "?": return "Sure.";
    return "Whatever."
