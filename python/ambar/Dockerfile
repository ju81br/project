FROM debian:jessie-slim

RUN apt update \
        && apt install -y \
               python3.4 \
               python3-pip \
               python3-dev \
               python3-setuptools \
               libaio-dev \
	  && pip3 install --upgrade pip \
	  && ln -s /usr/bin/python3.4 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

# set the working directory in the container to /app
WORKDIR /app

# set flask env
ENV FLASK_APP app.py

# because Python 3 was configured to use ASCII
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 5000 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
CMD ["flask", "run"]