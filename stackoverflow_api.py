import requests
import json
import webbrowser


from datetime import datetime, timedelta


def get_params(days: int = 7, min_votes: int = 5, tagged: str = "python"):

    timeBefore = timedelta(days=int(days))
    searchDate = datetime.today() - timeBefore

    params = {
        "site": "stackoverflow",
        "sort": "votes",
        "order": "desc",
        "fromdate": int(searchDate.timestamp()),
        "tagged": tagged,
        "min": int(min_votes)
    }

    return params


def save_web_pages(params):

    r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

    try:
        questions = r.json()
    except json.decoder.JSONDecodeError:
        print("Wrong format")
    else:
        return questions
        # for question in questions["items"]:
        #


def open_new_pages():
    with open("temp_pages.txt", "r", encoding="UTF-8") as file:
        for line in file:
            webbrowser.open_new_tab(line)


def save_current_to_file():
    with open("temp_pages.txt", "r", encoding="UTF-8") as file:
        text = file.readlines()
        for t in text:
            with open("saved_pages.txt", "a+", encoding="UTF-8") as file2:
                file2.write(t)
