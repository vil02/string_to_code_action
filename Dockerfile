FROM python:3-slim AS builder

RUN pip install --target=./ string-to-code
FROM gcr.io/distroless/python3-debian10
COPY --from=builder ./ ./

FROM gcr.io/distroless/python3-debian10
ENV PYTHONPATH .
CMD ["./main.py"]
