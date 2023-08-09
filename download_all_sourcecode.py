from datetime import datetime
from dotenv import load_dotenv
from requests_html import AsyncHTMLSession
from time import sleep, time
from typing import List
from tqdm import tqdm
import logging
import os
import requests as r


API_RATE_LIMIT = 5
BASE_URL = "https://etherscan.io/contractsVerified/"
CONTRACTS_FILEPATH = './2022-10-18_recent-500-verified_contracts-etherscan.txt'
NUM_PAGES = 20 # hardcoding since it's limited to 500 recent contracts anyway. 25 items per page
SAVEDIR = './data/verified-contracts'


def main():
    # config env
    load_dotenv()
    # config logging
    logging.basicConfig(level=logging.INFO)
    l = logging.getLogger('Main')
    l.setLevel(level=logging.INFO)
    # config dirs
    date = datetime.now()
    source_savedir = os.path.join(SAVEDIR, str(date))
    os.makedirs(source_savedir, exist_ok=True)


    # load addresses
    l.info("Collecting addresses...")
    addresses = collect_addresses(savefile_label=date)
    l.debug(addresses)
    l.info(f'{len(addresses)} addresses collected.')

    l.info('Retrieving (and saving to disk) sources...')
    save_sources(addresses, source_savedir)
    l.info(f'All done. Saved source to {source_savedir}. Cya ;)')



def save_sources(addresses: List[str], savedir: str):
    """ download source and save, obeying rate limit"""

    i = 0
    last_batch_start = time()
    for addr in tqdm(addresses):
        i += 1
        i %= API_RATE_LIMIT
        if i == 0:
            if time() - last_batch_start < 1: 
                sleep(time() - last_batch_start)
            last_batch_start = time()

        res = get_source(addr)
        with open(os.path.join(savedir, f'{res["ContractName"]}_{addr}.sol'), 'w') as f:
            f.write(res["SourceCode"])

def get_source(address: str) -> dict:
    url = (
        'https://api.etherscan.io/api'
       '?module=contract'
       '&action=getsourcecode'
       f'&address={address}'
       f"&apikey={os.environ['ETHERSCAN_API_TOKEN']}"
    )
    try:
        res = r.get(url).json()['result'][0]
        res['Address'] = address
    except:
        print('whoops at ' + address)
        
    return res

# main()



start_datetime = datetime.now()

def collect_addresses(savefile_label) -> List[str]:
    """Collect and save recent 500 verified addresses from Etherscan. Returns addresses"""

    s = AsyncHTMLSession()

    addresseses = s.run(*[_mk_address_getter(s, p) for p in range(1, NUM_PAGES+1)])

    # concat array
    addresses = []
    for _addresses in addresseses:
        addresses += _addresses

    with open(os.path.join(SAVEDIR, f'addresses-{savefile_label}.txt'), 'w') as f:
        f.writelines(addresses)

    return addresses

def _mk_address_getter(s: AsyncHTMLSession, page_num: int) -> List[str]:
    async def getter():
        r = await s.get(f'{BASE_URL}{page_num}')

        return [a.text for a in r.html.find('table tr td:first-child a')]

    return getter
          

# html = r.get(URL).text
# soup = BeautifulSoup(html, 'lxml')
# addresses = [a.get_text() for a in soup.find_all('table tr td:first-child a')]
# with open('tmp.html', 'w') as f:
#     f.write(html)

# print(addresses)

main()