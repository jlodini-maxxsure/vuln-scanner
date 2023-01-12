FROM mikesplain/openvas

ADD . / /openvas/
RUN chmod +x /openvas/run_scan.py

CMD ["/openvas/run_scan.py"]