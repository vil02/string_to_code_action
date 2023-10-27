FROM python:3-slim AS builder

RUN pip install string-to-code

CMD ["python", "main.py"]
