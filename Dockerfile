FROM ubuntu:20.04
VOLUME ["/beancount", "/reports"]
ENV REPORT_TYPES "cash trial networth"
ENV BEANCOUNT_FILE "MyLedger.beancount"
RUN apt-get update && apt-get install -y\
    python3\
    python3-pip\
    build-essential
RUN pip3 install beancount python-dateutil
RUN apt-get purge -y build-essential && apt-get autoremove -y
RUN mkdir /dailyreport
COPY dailyreport.py /dailyreport/
CMD python3 /dailyreport/dailyreport.py /beancount/${BEANCOUNT_FILE} /reports ${REPORT_TYPES}