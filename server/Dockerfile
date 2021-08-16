FROM ubuntu:18.04
MAINTAINER laz

RUN apt-get update
RUN apt-get -y install apache2 python python-pip libapache2-mod-wsgi-py3
RUN pip install Flask

RUN mkdir src
ADD start.sh /
ADD ./*.py /src/
ADD app.wsgi /src/
#ADD chat_server.conf /etc/apache2/sites-available/
#RUN a2ensite chat_server.conf
#
#CMD ./start.sh
ADD start_native.sh /src
WORKDIR src
CMD ./start_native.sh

