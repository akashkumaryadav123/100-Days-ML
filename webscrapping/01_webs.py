import requests
import time
from fake_useragent import UserAgent
url ="https://www.glassdoor.co.in/Reviews/index.htm?filterType=RATING_OVERALL&page=999&overall_rating_low=4"

proxy_auth = 'c071936660f5aa2d7156:476cc9733201022f@gw.dataimpulse.com:823'
proxies = {
    'http' : f'http://{proxy_auth}',
    'https' : f'https://{proxy_auth}'
}

session=requests.Session()
time.sleep(2)
headers={
    'User-Agent': UserAgent().random,
    'Accept-language':"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    "Accept-encoding":"gzip, deflate, br, zstd",
    
    "Referer":"https://www.glassdoor.co.in/"

}
r=session.get(url,proxies=proxies,headers=headers)

with open("file.html","w") as f:
    f.write(r.text)