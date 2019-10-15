#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Candidate(object):
    """
    Candidates are for the image and html source files
    """
    def __init__(self, idx, img_path, source_html):
        self.idx = idx
        self.img_path = img_path
        self.source_html = source_html

    def get_idx(self):
        return self.idx

    def get_img(self):
        return self.img_path

    def get_source(self):
        return self.source_html

    def print_info(self):
        print ("IDX is {}, Img is {} and souce is {}".format(self.idx, self.img_path, self.source_html))


# Support functions
def read_crawl_candidates(dire):
    files = os.listdir(dire)
    if not dire.endswith('/'):
        dire = dire + '/'

    idxs = list()
    candidates = list()

    def get_idx(f):
        return f.split("..")[0]

    for f in files:
        if f.startswith('.'):
            continue
        idx = get_idx(f)

        if idx not in idxs:
            img_txt = dire + idx + '..screen.png'
            source_html = dire + idx + '..source.txt'
            can = Candidate(idx, img_txt, source_html)
            candidates.append(can)
            idxs.append(idx)

    return candidates


PhishTank_BrandMap = {1: 'PayPal', 2: 'eBay', 3: 'Chase', 4: 'HSBC', 5: 'Barclays', 6: 'Bank of America / MBNA', 7: 'Wells Fargo',
                      8: 'Other', 9: 'LaSalle', 12: 'M &amp; I', 13: 'Wachovia', 14: 'Citizens', 15: 'Ameritrade', 16: 'Regions',
                      17: 'Associated Bank', 18: 'Huntington', 19: 'Charter One', 20: 'Key Bank', 21: 'Washington Mutual',
                      22: 'Comerica', 23: 'Peoples', 24: 'US Bank', 25: 'Westpac', 26: 'NatWest', 27: 'Bendigo', 28: 'Amarillo',
                      29: 'Capital One', 30: 'Compass', 31: 'Crown', 32: 'CIBC', 33: 'DBS', 34: 'National City', 35: 'Salem Five',
                      36: 'RBC', 37: 'Nantucket Bank', 39: 'Franklin', 40: 'Bank of KC', 41: 'FHB', 42: 'Citibank',
                      43: 'TD Canada Trust', 44: 'BMO', 45: 'Bank of the West', 48: 'Fifth Third Bank',
                      50: 'First Federal Bank of California', 51: 'Alliance Bank', 53: 'Western Union', 55: 'Sky Financial',
                      56: 'WalMart', 57: 'Independent Bank', 58: 'Volksbanken Raiffeisenbanken', 59: 'e-gold',
                      60: 'Downey Savings', 61: 'Amazon.com', 62: 'IRS', 63: 'BB&amp;T', 64: 'Poste', 65: 'Career Builder',
                      66: 'MBTrading', 67: 'Interactive Brokers', 68: 'Accurint', 69: 'PNC Bank', 70: 'RBS', 71: 'Nedbank',
                      72: 'KCFCU (Kauai Credit Union)', 73: 'Banca di Roma', 74: 'Facebook', 75: 'Salesforce', 76: 'Google',
                      77: 'EPPICard', 78: 'MySpace', 81: 'Habbo', 82: 'Bradesco', 84: 'Scotiabank', 85: 'Tibia', 86: 'Steam',
                      87: 'CUA (Credit Union Australia)', 88: 'World of Warcraft', 89: 'Orkut', 90: 'Standard Bank Ltd.',
                      91: 'First National Bank (South Africa)', 92: 'ABSA Bank', 93: 'South African Revenue Service',
                      94: 'Groupon', 95: 'LivingSocial', 96: 'BloomSpot', 97: 'HomeRun', 98: 'BuyWithMe', 99: 'Tippr',
                      100: 'Plum District', 101: 'Zynga', 102: 'Egg', 103: 'First Direct', 104: 'Halifax',
                      105: 'Cariparma Credit Agricole', 106: 'Gruppo Carige', 107: 'Cartasi', 108: 'HMRC', 109: 'Santander UK',
                      110: 'AOL', 111: 'Yahoo', 112: 'Live', 113: 'Craigslist', 114: 'Playdom', 115: 'Playfish', 116: 'ZML',
                      117: 'Skype', 118: 'American Airlines', 120: 'Caixo', 121: 'Safra National Bank of New York',
                      122: 'Blizzard', 123: 'ING', 124: 'Bancasa', 125: 'Banco Real', 126: 'Cahoot', 127: 'NEXON',
                      128: 'Rabobank', 129: 'Visa', 130: 'Mastercard', 131: 'Centurylink', 132: 'Twitter', 133: 'ANZ',
                      134: 'RuneScape', 135: 'Itau', 136: 'TAM Fidelidade', 137: 'Cielo', 138: 'Caixa', 139: 'ABL', 140: 'Delta',
                      141: 'American Greetings', 144: 'ASB', 145: 'Tagged', 146: 'Co-operative Bank', 147: 'Smile Bank',
                      148: 'Nationwide', 149: 'Northern Rock', 150: 'CIMB Bank', 151: 'GTBank', 152: 'Littlewoods', 153: 'Very',
                      154: 'Hotmail', 155: 'Vodafone', 156: 'Capitec Bank', 157: 'US Airways', 158: 'Banco De Brasil',
                      159: 'otoMoto', 160: 'Allegro', 161: 'Nets', 163: 'Suncorp', 164: 'NAB', 165: 'ATO', 166: 'St George Bank',
                      167: 'Commonwealth Bank of Australia', 168: 'Orange', 169: 'Verizon', 170: 'ArenaNet', 171: 'GuildWars2',
                      172: 'Swedbank', 173: 'Metro Bank', 175: 'Nordea', 176: 'PKO', 177: 'Microsoft', 178: 'Banca Intesa',
                      179: 'Lottomatica', 180: 'Pintrest', 181: 'TSB', 182: 'Lloyds Bank', 183: 'Apple', 184: 'American Express',
                      185: 'Deutsche Bank', 186: 'Discover Card', 187: 'Discover Bank', 188: 'Diners Club', 189: 'AT&amp;T',
                      192: 'PagSeguro', 193: 'Tesco', 194: 'Dropbox', 195: 'Permanent TSB', 196: 'Discovery', 197: 'DHL',
                      199: 'USAA', 200: 'Netflix', 201: 'ABN', 202: 'Intesa Sanpaolo', 203: 'Kiwibank', 204: 'LinkedIn',
                      205: 'NetSuite', 206: 'WhatsApp', 207: 'Adobe', 208: 'Bank Millennium', 209: 'Aetna', 210: 'Blockchain',
                      211: 'Alibaba.com', 212: 'BT', 213: 'Uber', 214: 'Coinbase', 215: 'LocalBitcoins.com', 216: 'Paxful',
                      217: 'Bitfinex', 218: 'GitHub', 219: 'Credit Karma', 220: 'UniCredit', 221: 'Rackspace', 222: 'Xapo',
                      223: 'MyEtherWallet', 224: 'bitFlyer', 225: 'MyMonero'}
