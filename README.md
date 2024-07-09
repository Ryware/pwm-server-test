# pwm-server-test

API for list items from SQLite Database using Django 4.2.13

Steps to run it locally:
1. Install [Python 3.11](https://www.python.org/downloads/)
2. Install "virtualenv": `pip install virtualenv`
3. Create virtual environment: `virtualenv -p python3 venv`
4. Apply virtual environment: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run SQL migrations: `python3 manage.py migrate`
7. Add sample data to database: `python3 manage.py load_items`
8. Run server: `python manage.py runserver 0.0.0.0:8000`
9. Test API with `curl http://127.0.0.1:8000/api/items`

Steps to run it in Docker:
1. Run `docker run -p 8000:8000 -d $(docker build -q .)`
2. Test API with `curl http://127.0.0.1:8000/api/items
