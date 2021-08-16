FROM ubuntu:18.04
MAINTAINER laz

RUN apt-get update
RUN apt-get -y install curl python python-pip
RUN pip install pyyaml

RUN mkdir /src
COPY client.py /src
ADD interface/ /src/interface/
ADD config /src/config/
ADD log/ /src/log/
ADD logging/ /src/logging/
ADD netUtils/ /src/netUtils/
ADD t.yaml /src/

WORKDIR /src

CMD python client.py

