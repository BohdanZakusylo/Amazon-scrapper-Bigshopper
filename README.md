# Amazon Scraper

This project is a web scraper designed to extract data from Amazon's website. This Project was lead by employees of
BigShopper,
and was created by the group IT2-E from NHL Stenden Hogeschool. This scraper was written in python using the Django
framework and is capable of cacheing & scraping amazon for a variety of information which is then stored in mongoDB for
caching and postgres for scraped data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes. These instructions include prerequisites, a step-by-step installation guide, a tutorial on the usage, a list
of the dependencies and acknowledgements.
Further explanation of the code can be found in comments above specific sections

### Prerequisites

The things you need before installing the software.

* python 8+
* postgresql local
* mongoDB compass
* Git bash

### Installation

1. Enter the directory you would like to clone the repository to
2. Clone the repository with the following command

```
git clone https://github.com/bigshoppernl/amazon-scraper.git
```

3. Create a virtual environment with the following command

```
python -m venv myenv
```

4. Activate the virtual environment with the following command

On Windows

```
myenv\Scripts\activate
```

On macOS and Linux

```
source myenv/bin/activate
```

5. Download the contents of the Requirements.txt file using the following command

```
pip install -r requirements.txt
```

### Postgresql

Step 1: Download the postgres installer onto your computer. To do this go to www.postgresql.org/download/. Download the
newest version suitable for your operating system.

Step 2: Run the installer and insert a password to continue. This password will be used for all the databases that you
will create inside postgresql.

NB: You do not need to install anything from the Stack Builder, it is optional to do so, you can just cancel.

Step 3: Search "pgAdmin" and run the application. Inside you will find the server and you click on it. One of the drop
down options is Postgresql 16(this will be according to what version of postgresql you downloaded), select it and enter
the password you have picked in Step 2.

Step 4: Right click on database and create a new database and give it a name.

Step 5: Go to the amazon_scraper folder and then to the Bigshopper folder. Create a new file and name it "
local_settings.py".

Step 6: Open the file "local_settings.py.dist". In it you will find instructions that will help with completing Step 5.

Step 7: Insert your credentials in the "local_settings.py".

```
DB_NAME = "testing"
USER = "postgres"
PASSWORD = "qwerty"
HOST = "localhost"
PORT = "12345"

MONGO_DSN = "localhost:00001"
```

NB: "local_settings.py" is a .gitignore file because sensitive data is stored in there. The data above is dummy data for clearer explanation.

Step 8: Run the command in the terminal "python manage.py makemigrations"

Step 9: Run the command in the terminal  "python manage.py migrate"

Step 10: Run the command in the terminal  "python manage.py command 'amazon.nl' '(the product name/asin)'"

Step 11: Refresh the database, open your database, open schemas and then open the tables. Right click on the
scraper_app_product and navigate to view all rows. The product from Step 10 will be inside the table.

### MongoDB

Step 1: Download the MongoDB Community installer onto your computer. To do this go
to https://www.mongodb.com/try/download/community . Download the newest version suitable for your operating system.

Step 2: Run the installer

Step 3: Connect to MongoDB deployment hosted on MongoDB Atlas or hosted locally on your own machine.

## Usage

The parser starts working only when special command is called. The example of this command will be show below.

```
$ python3(python) manage.py command "amazon.{country code}" "{title or gtin} {headless}"
$ python3(python) manage.py command "amazon.nl" "1234567891011 --headless" 
```

Note, that the first parameter has to be to amazon with the desired country code
and second parameter after the command should be strings, and should be placed in "".
The second parameter can be a GTIN/ASIN identifier or a product name.
The third parameter is either --headless either nothing. If u put --headless the selenium parser will work in headless mode, 
so you will not see the browser.
Please note that due to our algorithm the product name needs to be specific.
For example instead of "ps5" write "playstation 5 digital edition" for an accurate search

Instead of the "amazon.nl" there is also a possibility to scrape data from amazon.de and amazon.com.

After the output is received, it saves inside the postgres database and will be displayed on the page.
To access the page, run:

```
$ python3(python) manage.py runserver
```

The localserver will be started, and the link to the page will appear. On that link, the products from the database will
apper.

## Dependencies

* asgiref==3.7.2
* attrs==23.1.0
* certifi==2023.7.22
* charset-normalizer==3.3.1
* Django==4.2.6
* exceptiongroup==1.1.3
* h11==0.14.0
* idna==3.4
* Levenshtein==0.23.0
* lxml==4.9.3
* outcome==1.3.0.post0
* packaging==23.2
* psycopg==3.1.12
* psycopg2-binary==2.9.9
* PySocks==1.7.1
* python-dotenv==1.0.0
* python-Levenshtein==0.23.0
* rapidfuzz==3.4.0
* requests==2.31.0
* schedule==1.2.1
* selenium==4.14.0
* sniffio==1.3.0
* sortedcontainers==2.4.0
* sqlparse==0.4.4
* trio==0.22.2
* trio-websocket==0.11.1
* typing_extensions==4.8.0
* urllib3==2.0.7
* webdriver-manager==4.0.1
* wsproto==1.2.0

## Acknowledgments

* We would like to thank the organization BigShopper for letting us participate in a project with them
* We would like to give special thanks to Victor Zwart, Sietse Rijpstra, Arijen Zijlstra for helping us throughout this
  project