# -*- coding: utf-8 -*-

# shlom41k

import requests
from bs4 import BeautifulSoup
import json


class LiveScoreParser:

    @staticmethod
    def get_first_match(liga_link: str):
        pass

    @staticmethod
    def get_content(url: str):
        r = requests.get(url)
        return r.content


def get_html(url: str):
    r = requests.get(url)
    return r.text


def get_tables(html, some_liga=None):
    soup = BeautifulSoup(html, "lxml")

    ligas = soup.find_all("li", class_="match-accordion-item")

    all_stat = {}

    for liga in ligas:

        liga_name = liga.find("h3").text.strip()
        # print(f"Liga: {liga_name}")

        liga_tour = liga.find("td", class_="a-cherry").text.strip()
        # print(liga_tour)

        liga_matches = liga.find("table", class_="table-striped").find_all("tr")
        # print(liga_matches)

        games = {}

        for matches in liga_matches:
            try:
                com1, res, com2 = matches.find_all("a")

                command1 = com1.text.strip()
                command2 = com2.text.strip()
                result = res.text.strip()

                link = res.get("href")

                # print(command1, result, command2, f"link: {link}")
                games[f"{command1} <a href='{link}'>{result}</a> {command2}"] = link

            except:
                # print("Err read")
                pass

        all_stat[liga_name] = [liga_tour, games]

        if some_liga is not None:
            if some_liga == liga_name:
                return {liga_name: [liga_tour, games]}

    return all_stat


def get_ligas(url: str):
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    ligas = soup.find_all("li", class_="match-accordion-item")
    ligas_name = [liga.find("h3").text for liga in ligas]

    return ligas_name


def get_stat(url, liga=None):
    t = get_html(url)
    return get_tables(t, liga)


if __name__ == "__main__":
    url = "https://www.livescore.com/en/football/england/premier-league/fixtures/"

    page = LiveScoreParser.get_content(url)
    # print(page)

    soup = BeautifulSoup(page, "lxml")
    ligas = soup.find_all("div")
    print(ligas)
