FROM crawforc3/raspberrypi-uwsgi-nginx:latest
FROM crawforc3/raspberrypi-uwsgi-nginx-flask:latest

COPY ./app /app

RUN pip install flask-wtf
