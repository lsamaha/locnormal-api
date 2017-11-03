from debian

RUN apt-get -y update
RUN apt-get -y install curl autoconf automake make libtool python3-dev python3-pip pkg-config
RUN apt-get -y install git
RUN git clone https://github.com/openvenues/libpostal
RUN cd libpostal && sh ./bootstrap.sh
RUN mkdir /data
RUN cd libpostal && ./configure --datadir=/data
RUN cd libpostal && make
RUN cd libpostal && make install
RUN ldconfig
RUN pip3 install postal
RUN pip3 install flask
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["app.py"]
