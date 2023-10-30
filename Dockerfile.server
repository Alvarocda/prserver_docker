FROM ubuntu:20.04
WORKDIR /opt/pr/

EXPOSE 16567/tcp
EXPOSE 16567/udp
EXPOSE 29900/tcp
EXPOSE 29900/udp
EXPOSE 55123-55125/tcp
EXPOSE 55123-55125/udp

ENV DEBIAN_FRONTEND=noninteractive
# RUN sed -i -e 's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
RUN echo "deb http://security.ubuntu.com/ubuntu xenial-security main" >> /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -f
RUN apt-get install -f nano \
    python3 \
    python2 \
    libpython2.7 \
    libssl1.0.0 \
    python2.7 \
    libncurses5 \
    python3-pip \
    net-tools \
    software-properties-common \
    mumble-server -y
# RUN apt-get install python3-setuptools -y
# RUN easy_install3 pip
RUN cp /usr/lib/python2.7/hashlib.py /opt/pr
RUN pip3 install aiohttp
COPY ice34-slice_3.4.2-8.2_all.deb .
RUN dpkg -i ice34-slice_3.4.2-8.2_all.deb
RUN alias python=python3

RUN add-apt-repository ppa:rock-core/qt4
RUN apt-get update 
RUN apt-get install -y libqt4-declarative \
    qt4-dev-tools \
    qt4-qmake \
    libqtwebkit4

RUN echo 'alias python="python2"' >> ~/.bashrc
