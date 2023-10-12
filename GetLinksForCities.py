import time
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bson import ObjectId


base_url = "https://www.yellowpages.com/"
sitemap_url = base_url + 'sitemap'

mongo_client = MongoClient("localhost", 27017)['YellowPages']
db = mongo_client['states']
r = requests.get(sitemap_url)
time.sleep(2)
page_source = BeautifulSoup(r.text, "html.parser")
popular_cities = page_source.find("div", {"id": "all-states"})
for each_section_city in popular_cities.find_all('li'):
    each_a_tag = each_section_city.find_next('a')
    each_url = base_url + each_a_tag['href']
    print(each_a_tag.text, ">>", each_a_tag['href'])
    existing_document = db.find_one({"state_name": each_a_tag.text, "state_url": each_url})
    if existing_document is None:
        print(db.insert_one({"_id": ObjectId(), "state_name": each_a_tag.text, "state_url": each_url}))
