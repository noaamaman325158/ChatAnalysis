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


