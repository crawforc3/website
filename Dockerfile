FROM crawforc3/raspberrypi-uwsgi-nginx:latest
FROM crawforc3/raspberrypi-uwsgi-nginx-flask:latest

RUN pip install flask-wtf \
    flask-sqlalchemy

COPY ./app /app

