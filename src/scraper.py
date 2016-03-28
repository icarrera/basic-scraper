"""Basic html scraper for the King County food safety inspection website."""

import requests
import io
from bs4 import BeautifulSoup
import sys
import re


INSPECTION_DOMAIN = "http://info.kingcounty.gov"
INSPECTION_PATH = "/health/ehs/foodsafety/inspections/Results.aspx"
INSPECTION_PARAMS = {
    'Output': 'W',
    'Businesss_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
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
    'Sort': 'H'
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
    from_file = io.open(from_file, encoding='utf-8', mode='r')
    text = from_file.read()
    from_file.close()
    return text, 'utf-8'


def parse_source(html, encoding='utf-8'):
    """Setup the HTML as DOM nodes for scraping."""
    parsed = BeautifulSoup(html, 'html5lib')
    return parsed


def extract_data_listings(html):
    """Take parsed HTML and return list of restaurant listing container nodes."""
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


if __name__ == '__main__':
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98144'
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = load_inspection_page('inspection_page.html')
    else:
        html, encoding = get_inspection_page(**kwargs)
    doc = parse_source(html, encoding)
    print(doc.prettify(encoding=encoding))
