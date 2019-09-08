# Introduction

A django application to track the location of bikes and its status.

## Map Library
   [Leaflet.js](https://leafletjs.com/)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

Clone this project.
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

## CSV Data format

Reg. No.  |Location          |Ignition Status|   Fuel Level | Timestamp|
------------- | ------------- |------------- | ------------- | ------------- |
String  | <lat>T<long> |    True/False           |   0-100 |2018-12-25 09:27:53


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

