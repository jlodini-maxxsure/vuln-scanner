FROM mikesplain/openvas

ADD . / /openvas/
RUN chmod +x /openvas/run_scan.py
RUN apt-get -y install aws-cli

CMD ["/openvas/run_scan.py"]