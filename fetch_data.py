import json


def getUserData(userId):
    try:
        with open(f"users/{userId}.json") as f:
            return json.load(f)
    except:
        return None
