# StorageApp - A simple storage app

## Description
This app allow to manage a stock of "products" (could be anything) in a SQLite database. It is written in Python and uses the Django framework. This application is intended to be used in a local network, so it is not secure enough to be used in a production environment. And could be used as a template to create a more complex application.

## Features
- Create, edit and delete products
- Register of all the changes made to the products
- User authentication and management using the library [django-allauth](https://allauth.org/).
- Export the products to a CSV file (To Be implemented)
## Installation
1. Clone the [repository](https://github.com/jadry92/StorageApp):

```bash
git clone https://github.com/jadry92/StorageApp.git
```
2. Create a virtual environment and activate it:

Mac and Linux:
```bash
python -m venv venv
source venv/bin/activate
```
Windows:
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. migrate the database

```bash
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the server

```bash
python manage.py runserver
```

## Models

### Product
| Field | Type | Description |
| --- | --- | --- |
| name | CharField | Name of the product |
| description | TextField | Description of the product |
| stock | OneToOneField | Quantity model |
| created_at | DateTimeField | Date and time of the creation of the product |
| updated_at | DateTimeField | Date and time of the last update of the product |

### Stock

| Field | Type | Description |
| --- | --- | --- |
| quantity | IntegerField | Quantity of the product in the stock |
| created_at | DateTimeField | Date and time of the creation of the stock |
| updated_at | DateTimeField | Date and time of the last update of the stock |

### Transactions
| Field | Type | Description |
| --- | --- | --- |
| User | ForeignKey | User that made the change |
| Description | TextField | Description of the change |
| created_at | DateTimeField | Date and time of the creation of the transaction |
| updated_at | DateTimeField | Date and time of the last update of the transaction |


## references
- [Django documentation](https://docs.djangoproject.com/en/4/)
- [django-allauth documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)
