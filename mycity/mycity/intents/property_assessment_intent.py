"""
Intent to pull the assessed property values for Boston addresses



Get a property's most recent tax assessed value

Sample query:
https://www.cityofboston.gov/assessing/search/?q=1+longfellow+place

"""

from .custom_errors import \
    InvalidAddressError, BadAPIResponse, MultipleAddressError
from streetaddress import StreetAddressParser
from mycity.mycity_response_data_model import MyCityResponseDataModel
from mycity.intents.user_address_intent import clear_address_from_mycity_object

from . import intent_constants
import mycity.intents.speech_constants.trash_intent as speech_constants
import logging

import re

import requests
from bs4 import BeautifulSoup

from mycity.mycity_response_data_model import MyCityResponseDataModel

BASE_PAGE_TO_SCRAPE_URL = "https://www.cityofboston.gov/assessing/search/?"
# ASSESSMENT_BASE_URL = 'https://www.cityofboston.gov/assessing/search/?'
built_property_url = ASSESSMENT_BASE_URL + 'q=1+longfellow+place'


# logger = logging.getLogger(__name__)


def get_property_assessment_intent(mycity_request):
    """"""

    mycity_response = MyCityResponseDataModel()

    """
    This section taken from the Trash Intent
      - it retrieves the address from the session variables if present

    """
    # if intent_constants.CURRENT_ADDRESS_KEY in mycity_request.session_attributes:
    #     current_address = mycity_request.session_attributes[intent_constants.CURRENT_ADDRESS_KEY]
    #     print(current_address)  # Print for test
    #
    #     # grab relevant information from session address
    #     address_parser = StreetAddressParser()
    #     a = address_parser.parse(current_address)
    #
    #     print(a)  # Print for test
    #     # currently assumes that trash day is the same for all units at
    #     # the same street address
    #     address = str(a['house']) + " " + str(a['street_full'])
    #     zip_code = str(a["other"]).zfill(5) if a["other"] else None
    #
    #     print(address)  # Print for test
    #
    #     zip_code_key = intent_constants.ZIP_CODE_KEY
    #     if zip_code is None and zip_code_key in \
    #             mycity_request.session_attributes:
    #         zip_code = mycity_request.session_attributes[zip_code_key]

    # TODO: Get the users voice / speech data into the application, parsed, for the constructed / query string

    # constructed_string = (BASE_PAGE_TO_SCRAPE_URL + '')
    # scrape_assessed_value(constructed_string)

    mycity_response.session_attributes = mycity_request.session_attributes

    mycity_response.output_speech = "This is a test, this is only a test"

    mycity_response.card_title = "Boston Property Tax Assessment"
    mycity_response.reprompt_text = None
    mycity_response.should_end_session = True
    return mycity_response


def scrape_assessed_value(url):
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

