"""
Get a property's most recent tax assessed value

Sample query:
https://www.cityofboston.gov/assessing/search/?q=1+longfellow+place

"""


import re

import requests
from bs4 import BeautifulSoup


ASSESSMENT_BASE_URL = 'https://www.cityofboston.gov/assessing/search/?'


built_property_url = ASSESSMENT_BASE_URL + 'q=1+longfellow+place'


def main():
    get_and_parse(built_property_url)
    return


def get_and_parse(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html5lib")
    property_values = soup.find_all('td', string=re.compile("\$.*"))
    # print(len(property_value))
    print(property_values)  # Need to create a list in case more than one record is returned
    text_array = []
    for i in property_values:
        print(i)
        # text = i.find('td', string=re.compile("\$.*")).text
        # print(text)
    # return property_value


if __name__ == "__main__":
    main()
