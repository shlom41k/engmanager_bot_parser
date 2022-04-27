# -*- coding: utf-8 -*-

# shlom41k

import json


# bot settings
SETTINGS_JSON = "settings.json"


# Shlom41k is superuser. Insert your own chatID here.
SHLOM41k = 363543404

# settings format from settings.json is:
"""
settings_format = {
    "token": "token",
    "url": "http://link",
    "log_file": "path_to_logfile",

    "admins": {
        "chat_id": ["username", "firstname", "lastname"]
    },

    "users_authorized": {
        "chat_id": ["username", "firstname", "lastname"]
    },

    "users_unauthorized": {
        "chat_id": ["username", "firstname", "lastname"]
    },
}
"""

LIVE_SCORE_LEAGUES_URLs = {
    "England": "https://www.livescore.com/en/football/england/premier-league/fixtures/",
    "Germany": "",
}


def save_settings(data: dict, filename: str):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_settings(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def get_settings(data: dict) -> list:
    return [data[key] for key in data.keys()]


def update_settings(**kwargs) -> dict:
    data = {key: value for key, value in kwargs.items()}
    return data


if __name__ == "__main__":
    pass

