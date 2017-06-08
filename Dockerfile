FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:fontforge/fontforge
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y git cmake g++ pkg-config libcairo2-dev libpoppler-dev libpoppler-private-dev libfontforge-dev libspiro-dev


RUN cd /home && git clone --depth=1 git://github.com/coolwanglu/pdf2htmlEX.git
RUN cd /home/pdf2htmlEX && cmake . -DENABLE_SVG=ON && make -j && make install


RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install flask

RUN echo "tmpfs /tmp tmpfs defaults,size=32M 0 0" >> /etc/fstab

COPY webserver.py /tmp/webserver.py
COPY process_stdin.py /tmp/process_stdin.py

CMD python3 /tmp/webserver.py
