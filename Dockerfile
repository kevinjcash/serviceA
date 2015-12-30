# serviceA
FROM debian
MAINTAINER Kevin Cashman

EXPOSE 5000

RUN apt-get update && apt-get install -y \
        python \
        python-dev \
        python-pip \
    && apt-get clean
RUN pip install flask requests
RUN mkdir /opt/app

ADD hello.py /opt/app/hello.py

CMD /usr/bin/python /opt/app/hello.py $b_instance
