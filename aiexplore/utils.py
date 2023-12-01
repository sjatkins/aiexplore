from dotenv import find_dotenv, load_dotenv

loaded = [False]
def load_env():
    global loaded
    if not loaded[0]:
        _ = load_dotenv(find_dotenv())
        loaded[0] = True
    return loaded[0]


