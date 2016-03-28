# -*- coding: utf-8 -*-
import requests
import io
from bs4 import BeautifulSoup


DATA = 'kc_health_data.html'
INSPECTION_DOMAIN = "http://info.kingcounty.gov"
INSPECTION_PATH = "/health/ehs/foodsafety/inspections/Results.aspx/"
# see uri query output for inspection params
INSPECTION_PARAMS = {
    'Output': 'W',
    'Businesss_Name': '',
    'Business_Address': '',
    'Latitude': '',
    'Longitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'B'

}


def get_inspection_page(**kwargs):
    """Fetch a set of search results."""
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.content, resp.encoding


def load_inspection_page(from_file):
    """Load inspection page from  file."""
    from_file = io.open(from_file, encoding='utf-8', mode='read')
    text = from_file.read()
    from_file.close()
    return text, 'utf-8'
