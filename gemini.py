import os, json, sys
import google.generativeai as gemini


class GenAI:
    def __init__(self, credentials: dict, settings: dict, guide: str):
        self.credentials = credentials

        if self.credentials['api-key'] is None:
            self.printe("APIKeyError", f"Please get an API key from \033[1m{guide}\033[0m] and add it to the settings.json file to proceed further.")
            exit(1)

        gemini.configure(api_key=self.credentials['api-key'])

        self.txt_model = gemini.GenerativeModel(model_name=self.credentials['model-name'], generation_config=settings)
        self.chat_session = self.txt_model.start_chat(history=[])

        # self.img_model = gemini.GenerativeImageModel(self.credentials['model-name'])

    def printe(self, error_type: str, error_txt: str):
        print(f"\033[1;31m[-] {error_type}:\033[0m \033[1m{error_txt}\033[0m")

    def prints(self, success_type: str, success_txt: str):
        print(f"\033[1;32m[+] {success_type}:\033[0m \033[1m{success_txt}\033[0m")

    def printw(self, txt: str):
        print(f"\033[1;33m[*]\033[0m \033[1m{txt}\033[0m")

    def generate_text(self, prompt: str):
        return self.chat_session.send_message(prompt).text
