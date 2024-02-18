import json
import pytest
from run import app

def test_search():
    client = app.test_client()

    test_set = [
        ('Wei Strike Force', 'https://cards.scryfall.io/normal/front/0/b/0b4cc234-f6b7-4801-a6d0-c98b72f446cf.jpg?1562897354'),
        ('Marang River Prowler', 'https://cards.scryfall.io/normal/front/4/9/491a3dc5-d297-47e1-acf9-dda103136519.jpg?1604192521')
    ]

    body = {'cards': [d[0] for d in test_set], 'format': 'normal'}
    resp = client.post('/image', json=body)

    assert resp.status_code == 200

    urls = resp.json
    for i in range(len(test_set)):
        assert urls[i] == test_set[i][1]
