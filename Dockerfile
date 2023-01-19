FROM mikesplain/openvas

ADD . / /openvas/
RUN chmod +x /openvas/run_scan.py
RUN chmod +x /openvas/dynamo/sync.py
RUN chmod +x /openvas/start.sh
RUN pip install botocore boto3
RUN pip install botocore boto3 -t /openvas

CMD ["/openvas/start.sh"]