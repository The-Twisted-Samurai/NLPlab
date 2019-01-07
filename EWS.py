from newsstream import titles, bodies  
from textcleaner import cleantexts, cleantext
from pos_tagger import nlp, pos_list
import csv 
from db_tools import remove_duplicates, clean_db
headlines = titles 
summaries = bodies
pos_list(headlines)
