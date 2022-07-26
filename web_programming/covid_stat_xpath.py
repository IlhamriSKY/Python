# fetching covid 19 dari wordlmeters menggunakan lxml
from collections import namedtuple

import requests
from lxml import html  # type: ignore

covid_data = namedtuple("covid_data", "cases deaths recovered")


def covid_stats(url: str = "https://www.worldometers.info/coronavirus/") -> covid_data:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    return covid_data(*html.fromstring(requests.get(url).content).xpath(xpath_str))


fmt = """total kasus covid 18 di dunia: {}
total kematian akibat covid di dunia: {}
total sembuh dari covid : {}"""
print(fmt.format(*covid_stats()))
