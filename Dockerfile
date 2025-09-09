FROM python:3.12.3

WORKDIR /app

COPY app/ ./app/
COPY datasets/top-1m.csv ./datasets/top-1m.csv
COPY models/ ./models/
COPY preprocessing/ ./preprocessing/
COPY utils/ ./utils/
COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python utils/setup_nltk.py

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.app:app"]
