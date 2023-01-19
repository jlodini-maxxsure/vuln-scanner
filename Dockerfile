FROM mikesplain/openvas

ADD . / /openvas/
RUN chmod +x /openvas/run_scan.py
RUN chmod +x /openvas/dynamo/sync.py
RUN pip3 install boto3 -t /openvas/dynamo/
RUN chmod +x /openvas/start.sh

CMD ["/openvas/start.sh"]