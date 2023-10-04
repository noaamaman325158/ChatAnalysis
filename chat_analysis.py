import regex
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator

def date_time(s):
    #day/month/year | day\month\year
    pattern = '^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)(AM|PM|am|pm)? -'
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
    date, time = dateTime.split(', ')

    message = " ".join(splitline[1:])
    author = None  # Initialize author to None

    if find_author(message):
        splitmessage = message.split(": ")
        if len(splitmessage) == 2:
            author = splitmessage[0]
            message = splitmessage[1]

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

#Convert the data from the file into the data frame
df = pd.DataFrame(data, columns=["Date","Time","Author","Message"])
df['Date'] = pd.to_datetime(df["Date"])
print(df.tail(20))
print(df.Author.unique())
total_messages = df.shape[0]
print(total_messages)


media_messages_df = df[df["Message"] == '<Media ommitted>']
messages_df = df.drop(media_messages_df.index)
messages_df['Letter_Count'] = messages_df['Message'].apply(lambda s: len(s))
messages_df['Word_Count'] = messages_df['Message'].apply(lambda s: len(s.split(' ')))
messages_df['MessageCount'] = 1

#The 'I' variable list is represents the participants in the conversations
I = [' Noaa Maman' ,' +12 345 678 7890']

for i in range(len(I)):
    # Filtering out messages of a particular user
    req_df = messages_df[messages_df["Author"] == I[i]]

    # req_df will contain messages of only one particular user
    print(f"State of {I[i]} -")

    # shape will print the number of rows which indirectly means the number of messages
    message_count = req_df.shape[0]
    print('Messages Sent ', message_count)

    if message_count > 0:
        # Word Count contains the total words in one message, Sum of all words/Total Messages
        # Will yield words per message
        words_per_message = (np.sum(req_df['Word_Count'])) / message_count
        print('Average Words per message', words_per_message)
    else:
        print('No messages sent by this user.')
