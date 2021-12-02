FROM python

# set work directory
WORKDIR /home/intime/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /home/intime/app
RUN pip install -r /home/intime/app/requirements.txt

# copy project
COPY . /home/intime/app