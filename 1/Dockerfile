FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3.5
RUN apt-get install -y python3-pip
RUN pip3 install flask
COPY sample.py /home/
EXPOSE 5000
ENTRYPOINT ["/usr/bin/python3", "/home/sample.py"]