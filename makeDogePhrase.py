import os
import random

suffix = ["","!","!!","","!!!"]
dogeWords = ["DOGE WORDS GO HERE!"]
dogeColors = ["#ff1744"]

def hex_to_rgb(hex):
  hex = hex.lstrip('#')
  hlen = len(hex)
  return tuple(int(hex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))

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

def dogeColor():
    return hex_to_rgb(random.choice(dogeColors))
