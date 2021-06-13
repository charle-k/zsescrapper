from datetime import datetime

import requests
from bs4 import BeautifulSoup


url = "https://www.zse.co.zw/price-sheet/"



def get_zse_data():
    result = []
    sale_date = None

    page = requests.get(url)
    print('Price Sheet page collected...')

    if page.status_code == 200:
        print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """)
        print(page.content)
        print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """)

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

