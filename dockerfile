FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py migrate
RUN python3 manage.py load_items

EXPOSE 8000



CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
