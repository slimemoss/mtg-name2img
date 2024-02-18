import requests

class Search:
    def __init__(self):
        self.update()

    def update(self):
        self.nameImageDic = download()

    def image(self, cards, imageFormat='small'):
        return [self.nameImageDic[n][imageFormat] for n in cards]

def download():
    bulkUrl = 'https://api.scryfall.com/bulk-data/oracle-cards'
    d = requests.get(bulkUrl).json()
    download_url = d['download_uri']

    oracleData = requests.get(download_url).json()

    nameImagePair = dict()
    for d in oracleData:
        name = d['name']
        urls = d.get('image_uris', None)
        
        nameImagePair[name] = urls

    return nameImagePair
