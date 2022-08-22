FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt 
COPY foodgram/ .
CMD ["gunicorn", "foodgram.wsgi", "--bind", "0:8000" ]