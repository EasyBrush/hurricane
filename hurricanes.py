# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:44:27 2019

@author: Bryan
"""


import sqlite3
from bs4 import BeautifulSoup as bs
import pdb
#opens sql to get access to database
conn = sqlite3.connect("hurricane.db")
c = conn.cursor()

c.execute('select * From atlantic_hurricans' )
print(c.fetchall())
#year, tropical_storms, hurricanes, major_hurricanes, deaths, damage, notes

#open html file
with open ("atlantic.html", "rb" ) as file:
    soup = bs(file, 'lxml')
    
    table = soup.find_all('table')
    print(type(table), len(table))
    
    #pulls one table at a time
    for tabl in table[2:-1]:

        #pulls each row of table, excluding header row
        for row in tabl.find_all('tr')[1:]:
            #pull each column
            data = row.find_all('td')
            datas = [x.get_text().strip() for x in data]
            print(datas[0])
            if datas[0].get_text() == "Total":
                print("do nothing")
            
            elif int(datas[0].get_text()) < 1900:                
                c.execute("""insert into 'atlantic_hurricans' ('year', 'tropical_storms', 'hurricanes', 'major_hurricanes', 'deaths', 'damage', 'notes') values ('datas[0].get_text()', 'datas[2].get_text()', 'datas[3].get_text()','datas[4].get_text()', 'datas[5].get_text()', 0, 'datas[8].get_text()')""")
                conn.commit()
                
            else:
                print("happy")