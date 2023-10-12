import time
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bson import ObjectId

base_url = "https://www.yellowpages.com/"

mongo_client = MongoClient("localhost", 27017)['YellowPages']
db_states = mongo_client['states']
db_cities = mongo_client['states_cities']

for each_state in db_states.find():
    print(each_state)
    r_state = requests.get(each_state["state_url"])
    time.sleep(2)
    page_source = BeautifulSoup(r_state.text, "html.parser")
    state_paginator = page_source.find("section", {"class": "statepage-paginator"})
    # print(state_paginator)
    for each_link in state_paginator.find_all("a"):
        each_page_link = each_state['state_url']+each_link['href']
        print(each_page_link)
        r_cites = requests.get(each_page_link)
        time.sleep(1)
        r_page = BeautifulSoup(r_cites.text, "html.parser")
        list_content = r_page.find("div", {"class": "list-content row group"})
        # print(list_content)
        for each_li in list_content.find_all('a'):
            # print(each_li)
            # a_city = each_li.find_next('a')
            # print({"state": each_state['state_name'],
            #        "city": each_li.text,
            #        "link": each_state['state_url']+each_li['href']})
            existing_document = db_cities.find_one({"city": each_li.text,
                                                    "link": each_state['state_url']+each_li['href']})
            if existing_document is None:
                print(db_cities.insert_one({"_id": ObjectId(),
                                            "state": each_state['state_name'],
                                            "city": each_li.text,
                                            "link": each_state['state_url']+each_li['href']}))

        # print("----------------------------")
        # break
