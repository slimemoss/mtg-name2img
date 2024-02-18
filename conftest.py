import re
import json

import pytest
import httpretty

@pytest.fixture(scope="function", autouse=True)
def mock_http_request():
    httpretty.enable(verbose=True, allow_net_connect=False)

    blukUrl = 'https://api.scryfall.com/bulk-data/oracle-cards'
    with open('test_data/bulk-data.json') as f:
        d = json.load(f)
        d = json.dumps(d)
    httpretty.register_uri(httpretty.GET, blukUrl, body=d, status=200)
    

    cardsUrl = 'https://data.scryfall.io/oracle-cards/oracle-cards-20240217220152.json'
    with open('test_data/oracle-cards.json') as f:
        d = json.load(f)
        d = json.dumps(d)
    httpretty.register_uri(httpretty.GET, cardsUrl, body=d, status=200)

    
