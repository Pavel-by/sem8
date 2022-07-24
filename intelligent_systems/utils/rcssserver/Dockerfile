FROM ubuntu:20.04

ENV TZ=Europe/Moscow
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_17.x | bash -
RUN apt-get install -y git nodejs automake flex bison libtool build-essential libboost-all-dev

RUN git clone https://github.com/rcsoccersim/rcssserver.git /rcssserver
WORKDIR /rcssserver

RUN bash ./bootstrap && bash ./configure CXXFLAGS='-std=c++14'
RUN make && make install

RUN echo "\n/usr/local/share" >> /etc/ls.so.conf && \
ldconfig

EXPOSE 6000/udp

CMD rcssserver