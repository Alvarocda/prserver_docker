FROM ubuntu:20.04
WORKDIR /opt/pr/

EXPOSE 16567/tcp
EXPOSE 16567/udp
EXPOSE 29900/tcp
EXPOSE 29900/udp
EXPOSE 55123-55125/tcp
EXPOSE 55123-55125/udp


RUN echo "deb http://security.ubuntu.com/ubuntu xenial-security main" >> /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install nano python3 python2 libpython2.7 libssl1.0.0 python2.7 libncurses5 python3-pip net-tools -y
RUN cp /usr/lib/python2.7/hashlib.py /opt/pr
RUN pip3 install aiohttp