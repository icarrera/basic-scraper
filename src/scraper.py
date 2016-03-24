# -*- coding: utf-8 -*-
import requests

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


def get_inspection_page(data):
    """Fetch a set of search results."""
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in data.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.content, resp.encoding

def load_inspection_page(data):
    """Read file from disk and return the content."""
    
# get_inspection_page(INSPECTION_PARAMS)
