import requests
from bs4 import BeautifulSoup
import nltk

link = 'https://klimadao.medium.com/klima-dao-as-a-liquidity-engine-3a806ce5d3d5'
f = requests.get(link)
soup = BeautifulSoup(f.text,'html.parser')
page = soup.find_all("p")

with open('summary.txt', 'w') as scribe:
    for tag in page:
        paragraph = tag.get_text()
        sentences = nltk.tokenize.sent_tokenize(paragraph)
        print(paragraph)
        print('\n')
        scribe.write('\n')
        scribe.write("_______________")
        scribe.write('\n')
        scribe.write(sentences[0])
        scribe.write('\n')
        if len(sentences) > 1:
            scribe.write(sentences[-1])
        scribe.write('\n')
        scribe.write("_______________")
        scribe.write('\n')
