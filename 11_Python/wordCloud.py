""""
Name: Quyen Do
Assignment: 11_Python
File: wordCloud.py
Summary: text mining and create wordcloud in Python
"""


#Loading necessary libraries
import bs4
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 

# Read in the text
with open("constitution.txt","r") as docs:   
    soup = bs4.BeautifulSoup(docs,"lxml")
    text = soup.get_text()

# Convert text to lower case
text = text.lower()

# Create stopword list
stopwords = set(STOPWORDS)
stopwords.update(["section","article","the","shall","may"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords,background_color="white").generate(text)

#Display the generated image
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.savefig("python_Constitution_WordCloud.png")

""""
References:
https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
https://www.datacamp.com/community/tutorials/wordcloud-python
""""