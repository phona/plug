FROM alpine:3.7

EXPOSE 3031
WORKDIR /usr/src/app

RUN apk add --no-cache \
        uwsgi-python3 \
        python3 \
		postgresql-dev \
		gcc \
		python3-dev \
		musl-dev \
		linux-headers


COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . .

CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
               "--uid", "uwsgi", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "web:app" ]
