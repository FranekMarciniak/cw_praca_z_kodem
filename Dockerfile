FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]

