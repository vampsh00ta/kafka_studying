
FROM python:3

# set work directory
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt
# copy project
RUN chmod +x docker_entrypoint.sh
RUN ./docker_entrypoint.sh
COPY . .