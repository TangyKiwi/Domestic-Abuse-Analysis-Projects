import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/TangyKiwi/Worldie/master/RedHeart/Data/redheart_data_cleaned.csv")
stories = df["story"]

comment_words = ''
stopwords = set(STOPWORDS)
extra_stopwords = ["year", "old", "sentenced", "contact", "sherele", "red", "heart", "campaign", "please", "facebook", "map"]
for extra_stopword in extra_stopwords:
    stopwords.add(extra_stopword)

for story in stories:
    words = story.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    comment_words += " ".join(words) + " "

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = stopwords,
                      min_font_size = 10).generate(comment_words)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.savefig("../Wordclouds/stories_wordcloud.png")
