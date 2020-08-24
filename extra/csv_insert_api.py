import requests
import csv
import sys
from time import sleep

reload(sys)
sys.setdefaultencoding('utf8')

file = open('./data/marilia_dataset.csv', mode='r')
file = csv.reader(file, delimiter=';')

for row in file:
    category = row[0],
    attraction_name =  row[1],
    link_attraction = row[2],
    total_assessment = row[3],
    excellent_score =  row[4],
    great_score = row[5],
    fair_score = row[6],
    bad_score = row[7],
    horrible_score = row[8],
    address = row[9],
    web_site_external = row[10],
    phone = row[11],
    source_url = 'https://www.tripadvisor.com.br/'
    # print(row[0] + ' OK').decode('utf-8').strip()
    
    # Insert dataset on Rest Api ||POST||
    prod_url = "https://api-mvp-simbora.herokuapp.com/attractions/insert_new"


    attraction_data = {
        "category": category,   
        "attraction_name":attraction_name,
        "link_attraction":link_attraction,
        "total_assessment":total_assessment ,
        "excellent_score":excellent_score,
        "great_score":great_score,
        "fair_score":fair_score,
        "bad_score":bad_score,
        "horrible_score":horrible_score,
        "address":address,
        "web_site_external":web_site_external,
        "phone":phone,
        "source_url":source_url
    }


    sleep(3)
    response = requests.post(url=prod_url, json=attraction_data)

    if response.status_code == 200:
        #Success
        print(response.status_code)
        print(response.reason)
        print(response.text)
        # print(response.json())
        #print('Bytes', response.content)
    else:
        # Error
        print(response.status_code)
        print(response.reason)
        print(response.text)
        # print(response.json())
        #print('Bytes', response.content)

