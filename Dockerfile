FROM ubuntu:20.04
WORKDIR /opt/pr/

EXPOSE 16567/tcp
EXPOSE 16567/udp
EXPOSE 29900/tcp
EXPOSE 29900/udp
EXPOSE 55123-55125/tcp
EXPOSE 55123-55125/udp


RUN echo "deb http://security.ubuntu.com/ubuntu xenial-security main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install nano libpython2.7 libssl1.0.0 python2.7 libncurses5 -y

COPY ./prbf2_1.7.4.0_server .

RUN chmod u+x start_pr.sh
RUN chmod u+x start.sh
RUN chmod u+x start_with_docker.sh
RUN chmod u+x /opt/pr/bin/amd-64/prbf2_l64ded
RUN chmod u+x mods/pr/bin/prserverupdater-linux64
RUN cp /usr/lib/python2.7/hashlib.py /opt/pr/bin/amd-64/lib.linux-x86_64-2.7/

# RUN cd mods/pr/bin/ &&  yes '' | ./prserverupdater-linux64
ENV SERVER_PORT=16567
ENV MAX_PLAYERS=100
ENV SERVER_INTERNET=1
 
ENTRYPOINT [ "./start_with_docker.sh"]
