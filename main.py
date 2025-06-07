import json, os
from setup import Setup
Setup().main()

from head import Brain
from gemini import GenAI
from search import GSearch


mainDir = os.path.dirname(os.path.abspath(__file__))
settings_file = os.path.join(mainDir, 'settings.json')
man_file = os.path.join(mainDir, 'manual.txt')
guide_file = os.path.join(mainDir, 'guide.json')

guidance = dict(json.load(open(guide_file)))
settings = dict(json.load(open(settings_file)))
QUIT = settings['bot-commands']['quit']


def message_handler(txt: str) -> str:
    txt = txt.lower()
    ret = ""
    cmd = None

    brain = Brain(settings_file, man_file)
    genai = GenAI(settings['credentials']['gemini'], settings['GeminiAI'], guidance["gemini-api"])
    searchapi = GSearch(settings['credentials']['g-search'], guidance["g-search-api"])

    if ("search" in txt) or ("google" in txt):
        inpt = input("\033[1mSearch using \033[33mGoogle\033[0m\033[1m:\033[0m ").strip()
        ret = searchapi.search(inpt)

    elif ("genai" in txt) or ("gemini" in txt) or ("chatgpt" in txt):
        inpt = input("\033[1mSearch using \033[33mGemini\033[0m\033[1m:\033[0m ").strip()
        ret = genai.generate_text(inpt)

    else:
        ret, cmd = brain.think(txt)

    return ret, cmd


def main():
    RUN = True

    try:
        while RUN:
            inpt = input("\033[1mUser:\033[0m ").strip()
            resp, _cmd = message_handler(inpt)

            print(f"\033[1mBot:\033[0m {resp}\033[0m")

            if _cmd == QUIT:
                RUN = False

    except KeyboardInterrupt:
        print("\n\033[1mBot:\033[0m Ok, Bye")
        exit()


if __name__ == '__main__':
    main()
