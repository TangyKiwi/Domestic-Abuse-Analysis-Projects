import snscrape.modules.twitter as sntwitter
# https://github.com/JustAnotherArchivist/snscrape

import pandas as pd

query = "(from:elonmusk)"
tweets = []
limit = 10

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])
print(df)



