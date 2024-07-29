FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DOCKER_PORT=${DOCKER_PORT}

EXPOSE ${DOCKER_PORT}

CMD ["flask", "run"]