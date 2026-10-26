FROM python:3.16.0a1-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /main.py

CMD ["python", "/main.py"]
