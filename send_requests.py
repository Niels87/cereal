import requests
import requests.api
from prompt_toolkit import formatted_text, print_formatted_text, HTML
from html_parser import MyHTMLParser
from bs4 import BeautifulSoup


def send_request(self):
        
        param_dict = {
            "ids": [1,2],
            "username": "Niels"  
            }
        
        r = requests.get("http://localhost:8080/", params=param_dict)
        
        print(r.status_code)
        print(r.headers["content-type"])
        print("")        
        soup = BeautifulSoup(r.content.decode(), features="html.parser")
        #print(soup.prettify())
        
        for k in r.headers.keys():
            print(f"{k} : {r.headers[k]}")
        
        print("")
        
        print(r.raw)
        
        print("")
        
        for s in soup.strings:
            print(s)
            
        # for con in soup.descendants:
        #     print(con)

        #formatted = soup.prettify(formatter="html")
        
        #print(formatted)

        #print(soup.prettify())
    