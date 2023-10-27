FROM python:3-slim

RUN pip install string-to-code

COPY main.py /main.py
ENTRYPOINT ["/main.py"]
