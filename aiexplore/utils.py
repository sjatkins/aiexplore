from dotenv import find_dotenv, load_dotenv
from os import getenv

loaded = [False]
def load_env():
    global loaded
    if not loaded[0]:
        _ = load_dotenv(find_dotenv())
        loaded[0] = True
    return loaded[0]

def openai_key():
    load_env()
    return getenv('OPENAI_API_KEY')
