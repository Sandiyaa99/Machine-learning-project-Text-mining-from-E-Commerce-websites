#text mining word cloud
#pip install wordcloud
import requests
from bs4 import BeautifulSoup as bs
import re

import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud,STOPWORDS

#creating empty reviews list
amazon_reviews=[]
url="https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/product-reviews/B07HGGYWL6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
response=requests.get(url)
soup=bs(response.content,"html.parser")
reviews=soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})
for i in range(len(reviews)):
    amazon_reviews.append(reviews[i].text)
    
#writing reviews in a text file
with open(r"F:/MLP_SPYDER/amazon_review.txt","w",encoding='utf8')as output:
    output.write(str(amazon_reviews))
    
#joining all the reviews into single paragraph
ip_rev_string=" ".join(amazon_reviews)

#removing unwanted symbols incase if exists
ip_rev_string= re.sub("[^A-Za-z" "]+"," ",ip_rev_string).lower()
ip_rev_string= re.sub("[0-9" "]+"," ",ip_rev_string)
ip_rev_string

#convert the paragraph into single word
ip_reviews_words=ip_rev_string.split(" ")
ip_reviews_words

#here we are going to eliminate the stopping words
ip_reviews_words=[W for W in ip_reviews_words if not W in STOPWORDS]
ip_reviews_words

#joining all the reviews into single paragraph
ip_rev_string=" ".join(ip_reviews_words)
ip_rev_string

#wordcloud can be performed on the string inputs.that is the reason we have 
#entire reviews into single paragraph
wordcloud_ip=WordCloud(
                    background_color='white',
                    width=1920,
                    height=1080
                   ).generate(ip_rev_string)
plt.imshow(wordcloud_ip)
