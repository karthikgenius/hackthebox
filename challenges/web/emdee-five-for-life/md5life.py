import requests
import bs4
import hashlib

# Author: Karthik Sainadh
# CEH | PENTESTER | SECURIRY RESEARCHER
# twitter.com/karthikgenius19

url = "htpp://0.0.0.0:0000/" # Please Paste Your Target URL Here

sess = requests.Session()

raw_response = sess.get(url)

post_data = {"hash" : hashlib.md5(bs4.BeautifulSoup(raw_response.text, features="lxml").body.h3.text.encode("UTF-8")).hexdigest()}

raw_response = sess.post(url, post_data)

print(bs4.BeautifulSoup(raw_response.text, features="lxml").body.p.text)

sess.close()
