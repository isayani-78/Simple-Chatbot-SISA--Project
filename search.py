# from googlesearch import search
# from bs4 import BeautifulSoup
import requests, json


BLUE = 34


class GSearch:
    def __init__(self, credentials: dict, guide: str):
        self.search_url = "https://www.googleapis.com/customsearch/v1"
        self.params = {
            'q': None,
            'cx': credentials['id'],
            'key': credentials['api-key'],
        }

        if (credentials['api-key'] is None) or (credentials['id'] is None):
            print(f"\033[1;31m[-] APIKeyError:\033[0m \033[1mPlease get an API key from \033[1m{guide}\033[0m and add it to the settings.json file to proceed further.\033[0m")

    def search(self, query: str, indent: int = 4):
        self.params['q'] = query
        resp = requests.get(self.search_url, params=self.params).json()['items']
        res = {}
        ret = "{"

        for item in resp:
            res[item['title']] = item['link']

        for i, j in res.items():
            ret += f"{' '*indent}\"{i}\": \"\033[1;{BLUE}{j}\033[0m\",\n"

        ret += "}"

        return ret
