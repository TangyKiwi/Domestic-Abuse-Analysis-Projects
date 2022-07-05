import snscrape.modules.instagram as sninstagram
# https://github.com/JustAnotherArchivist/snscrape

# IG has insane rate limiting + IP bans, prob need different library
import pandas as pd

limit = 10
instagram = []
for item in sninstagram.InstagramUserScraper("elonmusk").get_items():
    if len(instagram) == limit:
        break
    else:
        instagram.append([item.date, item.content])

df = pd.DataFrame(instagram, columns=["Date", "Post Content"])
print(df)

