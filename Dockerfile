FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_RUN_PORT=80

EXPOSE 80/tcp

CMD [ "flask", "run", "--host=0.0.0.0" ]
