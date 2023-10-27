FROM cicirello/pyaction-lite:3

RUN pip install string-to-code

COPY main.py /main.py
ENTRYPOINT ["/main.py"]
