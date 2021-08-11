# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
WORKDIR /mysite
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000


CMD ["python", "manage.py", "makemigrations", "resume"]

CMD ["python", "manage.py", "makemigrations", "backend"]

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]