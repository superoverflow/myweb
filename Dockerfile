################################
# Docker build to run django
#
################################
FROM python:3.6-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CD apps
RUN [ "./manage.py", "runserver", "0.0.0.0:8000" ]