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


