FROM python:3

COPY . /app/

WORKDIR /app

ENV FLASK_APP=app.py

ENV FLASK_ENV=production

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python","app.py"]