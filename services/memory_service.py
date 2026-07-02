import json
from datetime import datetime

FILE = "data/history.json"


def save_memory(module, activity):

    try:
        with open(FILE, "r") as f:
            history = json.load(f)

    except:

        history = []

    history.insert(0, {

        "module": module,

        "activity": activity,

        "time": datetime.now().strftime("%d-%m-%Y %H:%M")

    })

    with open(FILE, "w") as f:

        json.dump(history, f, indent=4)


def load_memory():

    try:

        with open(FILE, "r") as f:

            return json.load(f)

    except:

        return []
        