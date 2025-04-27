FROM python:3.9-slim-buster

WORKDIR /app

COPY main.html .
COPY app.py .

EXPOSE 8000

CMD ["python", "app.py"]