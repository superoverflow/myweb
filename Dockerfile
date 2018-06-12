################################
# Docker build to run django
#
################################

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
