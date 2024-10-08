FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app/technews
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "technews.wsgi:application"]