from datetime import datetime, timedelta

import requests

timezone = 3


def get_past_matches(game, token, page_size=3):
    request = f"https://api.pandascore.co/{game}/matches/past"
    response = requests.get(request + "?token=" + token, params=f"page[size]={page_size}")
    result = []

    for el in response.json():
        el_result = []
        el_result.append(el.get("league").get("name"))
        el_result.append(el.get("serie").get("full_name"))

        for i in range(2):
            name = el.get("opponents")[i].get("opponent").get("name")
            score = el.get("results")[i].get("score")
            el_result.append(f"{name:15} {score}")

        begin_at = el.get("original_scheduled_at")
        if begin_at:
            begin_at = f"{begin_at[:10]} {begin_at[11:-1]}"
            begin_at = datetime.strptime(
                begin_at, "%Y-%m-%d %H:%M:%S") + timedelta(hours=timezone)
        el_result.append(begin_at)
        result.append(el_result)

    return result


def get_running_matches(game, token, page_size=3):
    request = f"https://api.pandascore.co/{game}/matches/running"
    response = requests.get(request + "?token=" + token, params=f"page[size]={page_size}")
    result = []

    for el in response.json():
        el_result = []
        el_result.append(el.get("league").get("name"))
        el_result.append(el.get("serie").get("full_name"))
        for i in range(2):
            name = el.get("opponents")[i].get("opponent").get("name")
            score = el.get("results")[i].get("score")
            el_result.append(f"{name:15} {score}")
        begin_at = el.get("begin_at")
        if begin_at:
            begin_at = f"{begin_at[:10]} {begin_at[11:-1]}"
            begin_at = datetime.strptime(
                begin_at, "%Y-%m-%d %H:%M:%S") + timedelta(hours=timezone)
        el_result.append(begin_at)
        el_result.append(el.get("streams").get("russian").get("embed_url"))
        result.append(el_result)

    return result


def get_upcoming_matches(game, token, page_size=3):
    request = f"https://api.pandascore.co/{game}/matches/upcoming"
    response = requests.get(request + "?token=" + token, params=f"page[size]={page_size}")
    result = []

    for el in response.json():
        el_result = []
        el_result.append(el.get("league").get("name"))
        el_result.append(el.get("serie").get("full_name"))
        el_result.append(el.get("name"))
        begin_at = el.get("begin_at")
        if begin_at:
            begin_at = f"{begin_at[:10]} {begin_at[11:-1]}"
            begin_at = datetime.strptime(
                begin_at, "%Y-%m-%d %H:%M:%S") + timedelta(hours=timezone)
        el_result.append(begin_at)
        result.append(el_result)

    return result
