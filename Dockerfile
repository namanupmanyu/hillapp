FROM python:3.10-slim

WORKDIR /app

RUN pip install Flask==2.3.3 gunicorn==20.1.0

COPY . .

EXPOSE 5001

CMD ["gunicorn", "-b", "0.0.0.0:5001", "app:app"]
