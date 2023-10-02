import regex
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator

def date_time(s):
    #day/month/year | day\month\year
    pattern = '^([0-9]+)(/\)([0-9]+)(/\)([0-9]+), ([0-9]+):([0-9]+)[]?(AM|PM|am|pm)? -'
    result = regex.match(pattern, s)

    if result:
        return True
    return False


def find_author(s):
    s = s.split(":")

    if len(s) == 2:
        return True
    else:
        return False
def getDataPoints(line):
    splitline = line.split('-')

    dateTime = splitline[0]
    date, time = dateTime.split.split(', ')

    message = " ".join(splitline[1:])
    if find_author(message):
        splitmessage = message.split(": ")
        message = " ".join(splitmessage[1:])
    else:
        author = None
    return date, time, author, message

data = []
conversation = "ChatExample.txt"
with open(conversation, encoding="utf-8") as fp:
    fp.readline()
    messageBuffer = []
    date, time, author = None, None, None
    while True:
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        if date_time(line):
            if len(messageBuffer) > 0:
                data.append([date, time, author, ' '.join(messageBuffer)])

            messageBuffer.clear()
            date, time, author, message = getDataPoints(line)
            messageBuffer.append((message))
        else:
            messageBuffer.append((line))





