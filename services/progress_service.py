import json

FILE = "data/study_progress.json"


def load_progress():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"today_hours": 0}


def save_progress(hours):
    with open(FILE, "w") as f:
        json.dump({"today_hours": hours}, f, indent=4)