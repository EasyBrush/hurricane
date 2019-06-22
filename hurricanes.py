# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:44:27 2019

@author: Bryan
"""

import pandas as pd
import sqlite3
from bs4 import BeautifulSoup as bs
import pdb
#opens sql to get access to database
conn = sqlite3.connect("hurricane.db")
c = conn.cursor()

c.execute('select * From atlantic_hurricans' )
print(c.fetchall())

#open html file
with open ("atlantic.html", "rb" ) as file:
    soup = bs(file, 'lxml')
    
    table = soup.find_all('table')
    print(type(table), len(table))
    
    #pulls one table at a time
    for tag in table[2:-1]:
        pdb.set_trace()
        #pulls the head
        head = tag.find_all('th')
        print("AAAA",head)
        #pulls items in header
        for header in head.find('tr'): 
            print(header)