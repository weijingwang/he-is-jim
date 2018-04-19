import os
import random

suffix = ["","!","!!","","!!!"]
dogeWords = ["DOGE WORDS GO HERE!"]
dogeColors = ["#ff5252","#ff4081","#e040fb","#7c4dff","#536dfe","#448aff","#40c4ff","#18ffff","#64ffda","#69f0ae","#b2ff59","#eeff41","#ffff00","#ffd740","#ffd740","#ff6e40","#ff1744","#f50057","#d500f9","#651fff","#3d5afe","#2979ff","#00b0ff","#00e5ff","#1de9b6","#00e676","#76ff03","#76ff03","#ffea00","#ffc400","#ff9100",""#ff3d00"]

def hexToRgb(hex_value):
    hex_value = normalize_hex(hex_value)
    hex_value = int(hex_value[1:], 16)
    return IntegerRGB(
        hex_value >> 16,
        hex_value >> 8 & 0xff,
        hex_value & 0xff
    )


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
    return hexToRgb(random.choice(dogeColors))

dogeColor()
