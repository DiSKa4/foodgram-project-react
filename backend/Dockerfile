FROM python:3.7-slim

WORKDIR /app

RUN pip install -r backend/requirements.txt 

COPY foodgram/ .

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]
