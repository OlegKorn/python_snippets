import requests
import re
from bs4 import BeautifulSoup as bs
import logging


FORMAT = '%(message)s'

file = "G:/Desktop/ЭКОЛОГИЯ/schule.txt"
path = "G:/Desktop/ЭКОЛОГИЯ/"

emails = ""

f = open(file, 'r').readlines()

logging.basicConfig(
    filename=f"{path}emails.log",
    level=logging.INFO, 
    format=FORMAT
)

for i in f:
    site = re.search("\"(.*?)\"", i).group(1)

    session = requests.Session()
    try:
        r = requests.get(site.strip())
    except Exception:
        print("===========")
        print(f"{site} is down")
        print("===========")
        continue 

    soup = bs(r.content, 'html.parser')

    try:
        mails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+', soup.text)
        if len(mails) > 0:
            for mail in mails:
                emails += mail + ", "

            print("===========")
            print(f"{site} ---------------------->>>>>>>>>>>>>>>>> {emails}")
            print("===========\n")
            logging.info(f"{emails}\n\n")

    except Exception as e:
        print(e)
        continue
