
## Installations

```bash
# clone the project
git clone https://github.com/adnankaya/django-iyzico.git
# go to project directory
cd django-iyzico
# create venv instance named as env
python3.11 -m venv env
# for linux/macos users
source env/bin/activate
# for windows users
.\env\Scripts\activate
# install packages
pip install -r requirements.txt
# create .env file and edit
cp .env.example .env
# Migrate files
python manage.py migrate
# [Optional] make migrations if necessary
python manage.py makemigrations app-name
python manage.py migrate
# run project for development mode
python manage.py runserver localhost:8000
```


### File Folders structure

```bash

├── README.md
├── db.sqlite3
├── manage.py
├── payments
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── services.py
│   ├── strategies
│   │   ├── __pycache__
│   │   ├── banktransfer
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── base.py
│   │   ├── creditcard
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── iyzico
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── dummy.py
│   │   │   ├── enums.py
│   │   │   ├── exceptions.py
│   │   │   └── utils.py
│   │   └── paypal
│   │       ├── __init__.py
│   │       └── __pycache__
│   ├── templates
│   │   └── payments
│   │       ├── base.html
│   │       ├── checkout.html
│   │       ├── index.html
│   │       ├── payment-failed.html
│   │       └── payment-success.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates
    ├── core.html
    └── index.html


```


### Mock test cards

Test cards that can be used to simulate a *successful* payment:

Card Number      | Bank                       | Card Type
-----------      | ----                       | ---------
5890040000000016 | Akbank                     | Master Card (Debit)  
5526080000000006 | Akbank                     | Master Card (Credit)  
4766620000000001 | Denizbank                  | Visa (Debit)  
4603450000000000 | Denizbank                  | Visa (Credit)
4729150000000005 | Denizbank Bonus            | Visa (Credit)  
4987490000000002 | Finansbank                 | Visa (Debit)  
5311570000000005 | Finansbank                 | Master Card (Credit)  
9792020000000001 | Finansbank                 | Troy (Debit)  
9792030000000000 | Finansbank                 | Troy (Credit)  
5170410000000004 | Garanti Bankası            | Master Card (Debit)  
5400360000000003 | Garanti Bankası            | Master Card (Credit)  
374427000000003  | Garanti Bankası            | American Express  
4475050000000003 | Halkbank                   | Visa (Debit)  
5528790000000008 | Halkbank                   | Master Card (Credit)  
4059030000000009 | HSBC Bank                  | Visa (Debit)  
5504720000000003 | HSBC Bank                  | Master Card (Credit)  
5892830000000000 | Türkiye İş Bankası         | Master Card (Debit)  
4543590000000006 | Türkiye İş Bankası         | Visa (Credit)  
4910050000000006 | Vakıfbank                  | Visa (Debit)  
4157920000000002 | Vakıfbank                  | Visa (Credit)  
5168880000000002 | Yapı ve Kredi Bankası      | Master Card (Debit)  
5451030000000000 | Yapı ve Kredi Bankası      | Master Card (Credit)  

*Cross border* test cards:

Card Number      | Country
-----------      | -------
4054180000000007 | Non-Turkish (Debit)
5400010000000004 | Non-Turkish (Credit)  

Test cards to get specific *error* codes:

Card Number       | Description
-----------       | -----------
5406670000000009  | Success but cannot be cancelled, refund or post auth
4111111111111129  | Not sufficient funds
4129111111111111  | Do not honour
4128111111111112  | Invalid transaction
4127111111111113  | Lost card
4126111111111114  | Stolen card
4125111111111115  | Expired card
4124111111111116  | Invalid cvc2
4123111111111117  | Not permitted to card holder
4122111111111118  | Not permitted to terminal
4121111111111119  | Fraud suspect
4120111111111110  | Pickup card
4130111111111118  | General error
4131111111111117  | Success but mdStatus is 0
4141111111111115  | Success but mdStatus is 4
4151111111111112  | 3dsecure initialize failed

