################################
# Docker build to run django
#
################################
FROM python:3.6-alpine
ENV APP_PORT=11080

COPY . /projects
WORKDIR /projects
RUN pip install -r requirements.txt

EXPOSE ${APP_PORT}
RUN cd apps && ./manage.py runserver 0.0.0.0:${APP_PORT}
