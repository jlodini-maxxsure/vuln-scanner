FROM mikesplain/openvas

ADD . / /openvas/
RUN chmod +x /openvas/run_scan.py
RUN chmod +x /openvas/dynamo/sync.py
RUN apt update -y && apt -y install curl
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py | python
RUN pip install boto3 -t /openvas/dynamo
RUN chmod +x /openvas/start.sh

CMD ["/openvas/start.sh"]