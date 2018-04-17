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
        dogeWord = dogeWords[random.randint(0, len(dogeWords))]

    print("dogeWord set to: " + dogeWord)

    print("generating suffix...")
    dogeSuffix = suffix[random.randint(0, len(suffix))]
    print("DogeSuffix set to: " + dogeSuffix)
    finalDogePhrase = dogeWord + dogeSuffix
    print("finalDogePhrase created: " + finalDogePhrase)

    return finalDogePhrase
