# https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/

from datetime import datetime

import requests
from bs4 import BeautifulSoup
import random

user_agent_list = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]


url = "https://www.zse.co.zw/price-sheet/"



def get_zse_data():
    result = []
    sale_date = None

    # Pick a random user agent
    user_agent = random.choice(user_agent_list)
    #print(user_agent)
    # Set the headers
    headers = {'User-Agent': user_agent}
    # Make the request

    page = requests.get(url, headers=headers)
    print('Price Sheet page collected...')

    if page.status_code == 200:
        print('Page collected.... code 200')
        #print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """)
        #print(page.content)
        #print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """)

        soup = BeautifulSoup(page.content, 'html5lib')

        # Get Date
        h4_tag = soup.h4
        span_tag = h4_tag.span
        dps = span_tag.string.split()[-3:]
        date_str = ' '.join(dps)
        sale_date = datetime.strptime(date_str, "%d %B %Y").date()

        # Table extractions
        table_data = soup.table.tbody
        count = 0
        trows = []
        for trow in table_data:
            if trow:
                res = str(trow).replace("\n", "")
                res2 = res
                res = res.lower()
                res = res.replace('<tr>', '')
                res = res.replace('</tr>', '')
                res = res.replace('<td>', '')
                res = res.replace('</td>', '')
                res.strip()
                if len(res) > 10:
                    count += 1
                    if count > 1:
                        trows.append(res2)

        for p in trows:
            soup = BeautifulSoup(p, 'html.parser')
            count = 0
            data = {}

            for td in soup.tr:
                count += 1
                r = td.string.strip()

                if count == 1:
                    data['name'] = r
                if count == 2:
                    r = r.replace(",", "")
                    data['opening'] = float(r)
                if count == 3:
                    r = r.replace(",", "")
                    data['closing'] = float(r)
                if count == 4:
                    r = r.replace(",", "")
                    if r.isdigit():
                        data['volume'] = int(r)
                    else:
                        data['volume'] = 0
            if len(data):
                result.append(data)

    return result, sale_date

