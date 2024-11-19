FROM python:3.11-slim

WORKDIR /app

COPY application.py /app

CMD ["python","application.py"]

