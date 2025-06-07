import json, os
from random import choice
from datetime import datetime


mainDir = os.path.dirname(os.path.abspath(__file__))
customCmds_file = os.path.join(mainDir, 'custom-cmds.json')


class Brain:
    def __init__(self, settings_file: os.path, manual_file: os.path):
        self.settings = dict(json.load(open(settings_file, "r")))
        self.settings['manual'] = open(manual_file, "r").read()
        self.customCmds = dict(json.load(open(customCmds_file, "r")))

        del self.settings['dependencies']

    def think(self, inpt: str):
        inpt = inpt.lower()
        ret = f"I don't understand what you said"
        cmd = None

        # Related to the BOT
        if "you" in inpt:
            if ("name" in inpt) or ("call" in inpt):
                ret = f"I am '{self.settings['name']}', your personal AI assistant."

            if ("age" in inpt) or ("years" in inpt) or ("old" in inpt):
                ret = f"My version is \033[1m{self.settings['version']}"

            if "description" in inpt:
                ret = f"{self.settings['description']}"

            if ("author" in inpt) or ("creator" in inpt) or ("dev" in inpt) or ("parent" in inpt) or ("mother" in inpt) or ("father" in inpt) or ("mom" in inpt) or ("dad" in inpt) or ("made" in inpt):
                ret = f"My creators are '{'\', \''.join(self.settings['author'].title())}'."

        if ("version" in inpt):
            ret = f"Version: \033[1m{self.settings['version'].upper()}"

        if ("man" in inpt) or ("help" in inpt):
            ret = self.settings['manual']

        # Greetings
        if ("hello" in inpt) or ("hi" in inpt) or ("hey" in inpt):
            ret = choice(self.customCmds['greetings'])

        if ("bye" == inpt) or ("goodbye" == inpt) or ("end" == inpt) or ("exit" == inpt) or ("kill" == inpt) or ("quit" == inpt) or ("stop" == inpt) or ("close" == inpt) or ("killall" == inpt) or ("finish" == inpt):
            ret = choice(self.customCmds['endings'])
            cmd = self.settings["bot-commands"]["quit"]

        if "how are you" in inpt:
            ret = f"I am fine, what about you?"

        # DateTime
        if "time" in inpt:
            ret = f"Right now it is {datetime.now().strftime('%H:%M:%S')}"

        if "date" in inpt:
            ret = f"Today is {datetime.now().strftime('%d-%m-%Y')}"

        return ret, cmd
