# props to code with harry and NEWSAPI 
# my personal news channel

import requests
import json
import time


print("*"*10,"POCKET HEADLINES","*"*10)
x = int(input("\nDo you want, TOP HEADLINES (Press 1) or Specific CATEGORY NEWS (Press 2)\nEnter:"))
match x:
    case 1:
        #TOP HEADLINES
        n = int(input("\nHow many headlines? TOP "))
        topurl = "https://newsapi.org/v2/top-headlines?country=in&apiKey=7bc4c2f26f1a4d10b3251fa31f1960e6"
        r = requests.get(topurl)
        news = json.loads(r.text)
        for i,art in enumerate(news["articles"]):
            print(f"Headline {i+1}: ",art["title"])
            print("\n",art["description"])
            print("-"*100)
            if (n-1)<=i:
                break
        
    case 2:
        #CATEGORY HEADLINES
        search = input("\nEnter the news category: ")
        n = int(input("How many headlines: "))
        curl = f"https://newsapi.org/v2/everything?q={search}&from=2024-03-26&sortBy=publishedAt&apiKey=7bc4c2f26f1a4d10b3251fa31f1960e6"
        r = requests.get(curl)
        news = json.loads(r.text)
        for i,art in enumerate(news["articles"]):
            print(f"Headline {i+1}: ",art["title"])
            print("\n",art["description"])
            print("-"*100)
            if (n-1)<=i:
                break

time.sleep(600)