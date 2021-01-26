import hashlib
import urllib3
from bs4 import BeautifulSoup
import requests

while(True):
    s=requests.Session()
    url = "http://docker.hackthebox.eu:31428/"

    page = s.get(url)
    soup = BeautifulSoup(page.content,"html.parser")

    #print(soup)
    stringInput = soup.find("h3").text.strip()

    #print(stringInput)

    result = hashlib.md5(stringInput.encode())

    answer = result.hexdigest()

    print(answer)

    answer = {'hash': str(answer)}

    cookies = {'ajs_anonymous_id':'%22858a875c-7666-4f10-8ba0-c5b54f524882%22','ajs_user_id':'%22d84277d258b4279b14dce9604b754979%22','PHPSESSID': 'j0la9en4h6eosm2nc75dcbggr4'}

    x = s.post(url = url, data = answer, cookies= cookies)

    print(x.text)


