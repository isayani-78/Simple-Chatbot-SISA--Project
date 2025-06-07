import requests, json
from colorama import Fore, Style, init

init(autoreset=True)

class GSearch:
    def __init__(self, credentials: dict, guide: str):
        self.search_url = "https://www.googleapis.com/customsearch/v1"
        self.params = {
            'q': None,
            'cx': credentials['id'],
            'key': credentials['api-key'],
        }

        if (credentials['api-key'] is None) or (credentials['id'] is None):
            print(f"{Fore.RED}[-] APIKeyError:{Style.RESET_ALL} {Style.BRIGHT}Please get an API key from {guide} and add it to the settings.json file to proceed further.")

    def search(self, query: str, indent: int = 4):
        self.params['q'] = query
        resp = requests.get(self.search_url, params=self.params).json()['items']
        res = {}
        ret = "{\n"

        for item in resp:
            res[item['title']] = item['link']

        for title, link in res.items():
            ret += f"{' ' * indent}\"{title}\": \"{Fore.BLUE}{link}{Style.RESET_ALL}\",\n"

        ret += "}"

        return ret