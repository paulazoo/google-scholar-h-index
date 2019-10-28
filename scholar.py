#selenium
from selenium import webdriver
#keyboard manipulation
from selenium.webdriver.common.keys import Keys
#folder manipulation
import os
#keep track of time
import time
#sound notifications (beeps)
import winsound


#ask for author input
#e.g. J. Julius Zhu
author = input('enter author name: ')
authorplus = author.replace(" ", "+")

#predefine h
h = 0
#predefine page as no page
page = 0
#predefine publication position
n = 0

#open webdriver chrome browser
driver = webdriver.Chrome('./chromedriver.exe')
#go to Google Scholar search first page for author
driver.get(('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C47&q=author%3A%22{}\"&btnG=').format(authorplus))
#wait to load webpage
time.sleep(1)


while h == 0:
    
    #wait to load webpage
    time.sleep(1)
    #new page
    page = page + 1
    
    #get all "Cited by " elements
    infos = driver.find_elements_by_xpath("//*[contains(text(), 'Cited by ')]")
    
    #do they think we're a robot?
    if len(infos) == 0:
        time.sleep(60)
        
    #go through each element to find citations
    for i in range(0,len(infos)-1):
        #single element
        elem = infos[i]
        #get the text of Cited by element
        text = elem.text
        #get out citation number from text
        clist = [int(c) for c in text.split() if c.isdigit()]
        c = clist[0]
        print('citations:' + str(c))
        #position number
        n = n + 1
        print('position: ' + str(n))
        #check if citation is still equal to or greater than n (h definition)
        if (c >= n):
            print(c)
        elif h == 0:
            h = n
            print('h index: ' + str(h))
            break
            
    #go to next Google Scholar search page for author
    #page = 1 loads 2nd page, page = 2 loads 3rd page
    driver.get(('https://scholar.google.com/scholar?start={0}0&q=author:%22{1}%22&hl=en&as_sdt=0,47').format(page, authorplus))

#close driver after finished
driver.close()
