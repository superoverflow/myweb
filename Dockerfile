################################
# Docker build to run django
#
################################
ENV APP_PORT=11080

FROM python:3.6-alpine
RUN apt-get install ffmpeg

COPY . /myweb
WORKDIR /myweb
RUN pip install -r requirements.txt

EXPOSE ${APP_PORT}
CMD cd apps && ./manage.py runserver 0.0.0.0:${APP_PORT}
