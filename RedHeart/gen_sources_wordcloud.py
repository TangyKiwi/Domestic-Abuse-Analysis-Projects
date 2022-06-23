import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/TangyKiwi/Worldie/master/RedHeart/redheart_data_cleaned.csv")
source1 = df["source1"]
source2 = df["source2"]

comment_words = ''
stopwords = set(STOPWORDS)

def gen_keywords(link, comment_words):
    req = requests.get(link)
    soup = BeautifulSoup(req.content, "html.parser")
    tokens = soup.text.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens) + " "
    return comment_words

# range(len(source1))
for i in range(25):
    if not pd.isnull(source1[i]):
        comment_words = gen_keywords(source1[i].strip(), comment_words)
        print(df["id"][i] + " (source1) : " + source1[i].strip() + " parsed")
    if not pd.isnull(source2[i]):
        comment_words = gen_keywords(source2[i].strip(), comment_words)
        print(df["id"][i] + " (source2) : " + source2[i].strip() + " parsed")

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = stopwords,
                      min_font_size = 10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()







