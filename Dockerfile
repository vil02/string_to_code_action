FROM python:3-slim

RUN pip install string-to-code

FROM gcr.io/distroless/python3-debian10
ENV PYTHONPATH .
CMD ["./main.py"]
