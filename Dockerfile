FROM python:3.5.3

WORKDIR /app

COPY . .

EXPOSE 5000

RUN pip install -r requiremets.txt

ENTRYPOINT '/usr/local/bin/python' 'app.py'
