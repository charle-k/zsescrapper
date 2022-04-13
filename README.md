# Zimbabwe Stock Exchange - Scrapping Price Sheet
Zsescrapper is a small django web application for scrapping Share Price Data
from the ZSE webpage https://www.zse.co.zw/price-sheet/

## Installation

Create your application directory and the clone the Repository:

```bash
git clone https://github.com/charle-k/zsescrapper.git .
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Virtual Environment

```bash
source venv/bin/activate
```

Apply Model Migrations

```bash
python manage.py migrate
```

Add a superuser

```bash
python manage.py createsuper
```

## Usage

Start server

```bash
python manage.py runserver
```

Open the website, on localhost: http://127.0.0.1:8000

## Scrapping latest Pricesheet
Login into site. On the front page you will now see a link to scrape data from www.zse.co.zw


## License
[MIT](https://choosealicense.com/licenses/mit/)



