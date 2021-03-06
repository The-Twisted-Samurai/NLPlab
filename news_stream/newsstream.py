# news API key: edfe8d41e6f84e93971ae5d76b0c805f
# TODO real time newsfeed from verified sources 
# TODO generate rich text files with the called data 
# TODO call tons of articles for training 
from newsapi import NewsApiClient
from classes import req_h, req_e
import ijson, json
import pandas as pd
import csv
import numpy as np
import datetime as dt


news = NewsApiClient(api_key='edfe8d41e6f84e93971ae5d76b0c805f')
report = str
articles = None
headlines = None 
summary = None
print("------------NewsAPI Stream OwO------------")
print(" ")
frm = input("Search query: ")
print(" ") 
print("fetching artices..")
print("") 
src = None

today = str(dt.datetime.now().date())

def get_trainingdata_TEST(req_h):
    global report
    report = news.get_everything(q= frm, sources= req_h.sources, language= req_h.language, to = req_h.to, sort_by= req_h.sortBy, page_size= req_h.pageSize)
    return report

def HELPER_generatestream(report):
    with open('nstream.json', 'w') as stream: 
        return json.dump(report, stream)

def getcontent():
    global articles
    global headlines
    global summary
    with open('nstream.json', 'r') as stream: 
        articlestream = ijson.items(stream, 'articles') 
        k = list(articlestream)
        articles = list(k[0])
        headlines = [title['title'] for title in articles ]
        summary = [sum['description'] for sum in articles]
        print('successfully fetched articles.')
        print("total headlines", len(headlines))
        print("total summaries", len(summary))
        print(" ")
        return headlines, summary

def generatestream(headlines, summary):
        stream = [headlines, summary]
        with open('newsstream.csv','w', newline = '', encoding = "utf-8" ) as newsstream:
            writer = csv.writer(newsstream, lineterminator='\n')
            writer.writerows(stream) 
        return 

def newsstream(req_h):
    # testdeploy(req_h)
    get_trainingdata_TEST(req_h)
    HELPER_generatestream(report)
    getcontent()
    return generatestream(headlines,summary)

trainer = req_h(q = None, sources = src, category = None, 
                language = 'en', country = None, to = today, sortBy = 'relevancy', 
                pageSize = 100)

newsstream(trainer)
display = input("Display headlines? [y/n]: ")
if display == "y":
        for headline in headlines:
                print("---")
                print(headline)
                print(" ")