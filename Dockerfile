FROM python:3-slim AS builder

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
