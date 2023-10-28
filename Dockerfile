FROM python:3-slim AS builder

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
