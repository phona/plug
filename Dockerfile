FROM python:3.6-slim

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 80

ENV NAME Upgrade

# CMD ["wsgi", "--ini", "/app/upgrade.ini"]
CMD ["python", "web.py"]
