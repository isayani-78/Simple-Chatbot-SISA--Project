import os, json, sys
import google.generativeai as gemini
from colorama import Fore, Style, init

init(autoreset=True)

class GenAI:
    def __init__(self, credentials: dict, settings: dict, guide: str):
        self.credentials = credentials

        if self.credentials['api-key'] is None:
            self.printe("APIKeyError", f"Please get an API key from {guide} and add it to the settings.json file to proceed further.")
            exit(1)

        gemini.configure(api_key=self.credentials['api-key'])

        self.txt_model = gemini.GenerativeModel(model_name=self.credentials['model-name'], generation_config=settings)
        self.chat_session = self.txt_model.start_chat(history=[])

    def printe(self, error_type: str, error_txt: str):
        print(f"{Fore.RED}[-] {error_type}:{Style.RESET_ALL} {Style.BRIGHT}{error_txt}")

    def prints(self, success_type: str, success_txt: str):
        print(f"{Fore.GREEN}[+] {success_type}:{Style.RESET_ALL} {Style.BRIGHT}{success_txt}")

    def printw(self, txt: str):
        print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} {Style.BRIGHT}{txt}")

    def generate_text(self, prompt: str):
        return self.chat_session.send_message(prompt).text