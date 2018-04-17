import os
import random

suffix = ["","!","!!","","!!!"]
dogeWords = ["DOGE WORDS GO HERE!"]

def dogeSay():
    firstDoge = random.randint(0, 40)
    if (firstDoge == 1):
        dogeWord = "wow"
    elif (firstDoge == "2"):
        dogeWord = "pls"
    else:
        dogeWord = random.choice(dogeWords)
    print("dogeWord set to: " + dogeWord)

    print("generating suffix...")
    dogeSuffix = random.choice(suffix)
    print("DogeSuffix set to: " + dogeSuffix)

    finalDogePhrase = dogeWord + dogeSuffix
    print("finalDogePhrase created: " + finalDogePhrase)

    return finalDogePhrase
