FROM python:3.10-slim as build

# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

# Working directory where all the setup would take place in the image
WORKDIR usr/app

RUN pip3 install --upgrade pip
RUN apt-get -y update


RUN apt-get install -y postgresql-client
RUN apt-get -y install curl
RUN export LC_ALL=C.UTF-8 && export LANG=C.UTF-8


# copy the Pipfile & pipfile.lock which contains dependencies to be installed
COPY requirements.txt .

# RUN pip install
RUN pip install -r requirements.txt

# USER root

COPY . .
EXPOSE 80
CMD ["/bin/bash", "-c", "docker/start_api.sh"]