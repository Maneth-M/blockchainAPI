import requests
from bs4 import BeautifulSoup


class BlockchainScrap:
    def __init__(self, address, page=1):
        self.address = address
        self.page = page
        self.url = f"https://www.blockchain.com/btc/address/{self.address}?page={self.page}"
        self.response = requests.get(self.url).content
        self.soup = BeautifulSoup(self.response, "html.parser")

    def get_transactions(self):
        lst = []
        for i in self.soup.findAll('div', {'class': 'sc-1fp9csv-0 ifDzmR'}):
            if "Unconfirmed" in i.text:
                continue
            if "Hash" in i.text:
                lst.append([(i.text.split("Date")[0].split("Hash")[1]), i.find('div', {'class': 'kad8ah-0 drlFvR'}).text])
        if not lst:
            return BlockchainScrap(self.address, page=self.page+1).get_transactions()
        return lst

