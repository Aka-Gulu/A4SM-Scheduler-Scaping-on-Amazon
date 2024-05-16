# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:09:23 2023

@author: Jensen R
"""

from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from datetime import datetime
import schedule




print ("Price & rating for gaming laptops on Amazon",str(datetime.now()))


def laptopprice():

    
    urls = [
        'https://www.amazon.com/s?k=gaming+laptop&i=electronics&rh=n%3A172282%2Cp_89%3AASUS%2Cp_72%3A1248879011&dc&ds=v1%3AC8vvQSPmCAup1VstI%2F0ZNRyIpEVbYxRctb6%2FAhqIvcc&crid=2M2GQ150I11PQ&qid=1700078772&rnid=1248877011&sprefix=gaming+laptop%2Caps%2C107&ref=sr_nr_p_72_1',
        'https://www.amazon.com/s?k=gaming+laptop&i=electronics&rh=n%3A172282%2Cp_89%3Amsi&dc&ds=v1%3A5Q9ht7GjfeyEM187N1mRpUARh%2B7n2UAl%2FkdEgR2hM2A&crid=2M2GQ150I11PQ&qid=1699932373&rnid=2528832011&sprefix=gaming+laptop%2Caps%2C107&ref=sr_nr_p_89_2',
        'https://www.amazon.com/s?k=gaming+laptop&i=electronics&rh=n%3A172282%2Cp_89%3Aacer%2Cp_72%3A1248879011&dc&crid=2M2GQ150I11PQ&qid=1700079028&rnid=1248877011&sprefix=gaming+laptop%2Caps%2C107&ref=sr_nr_p_72_1&ds=v1%3A%2F6EPEwgarP%2FCdxVsyFgzx5KUpdgCBT7nPtAE4wcoR5A',
        'https://www.amazon.com/s?k=gaming+laptop&i=electronics&rh=n%3A172282%2Cp_89%3AHP%2Cp_72%3A1248879011&dc&crid=2M2GQ150I11PQ&qid=1700078217&rnid=1248877011&sprefix=gaming+laptop%2Caps%2C107&ref=sr_nr_p_72_1&ds=v1%3AynAsF%2Fi7DelMYKJmF1RMb%2BqEr1UEf3NokieB0xy3TzM',
        'https://www.amazon.com/s?k=gaming+laptop&i=electronics&rh=n%3A172282%2Cp_89%3ALenovo%2Cp_72%3A1248879011&dc&crid=2M2GQ150I11PQ&qid=1700078022&rnid=1248877011&sprefix=gaming+laptop%2Caps%2C107&ref=sr_nr_p_72_1&ds=v1%3AQTc2fWYeR3nIPKEon6itVXjwNzvWfcdBbZthHceh3V0'
        ]

    for url in urls:

        browser = webdriver.Edge()

        # Open the URL
        browser.get(url)
        time.sleep(3)  # Wait for initial content to load

        # Get the page source
        html = browser.page_source
        browser.quit()  # Close the browser after scraping

        soup = bs(html, 'html.parser')
        currenttime = str(datetime.now())
        
        name=soup.find_all('span',class_="a-size-medium a-color-base a-text-normal")
        for i in name[0:5]:
            productname=i.text       
            print("product for", currenttime[0:19], " ","is:", productname)
            
            
        price=soup.find_all('span',class_="a-price-whole")
        for i in price[0:5]:
            productprice=i.text
            print("price for", currenttime[0:19], " ","is:", productprice)
            
            
        rating=soup.find_all('span',class_="a-icon-alt")
        for i in rating[0:5]: 
            productrating=i.text
            print("rating for", currenttime[0:19], " ","is:", productrating)
            
            
                
# Schedule the function to run daily at 14:50
schedule.every().day.at("02:10").do(laptopprice)

# Loop to keep the script running and check the schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking again



          