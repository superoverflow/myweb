################################
# Docker build to run django
#
################################
ARG PORT=11080

FROM python:3.6-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN cd apps && ./manage.py runserver 0.0.0.0:${PORT}
EXPOSE ${PORT}