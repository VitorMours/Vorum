FROM ubuntu/python:latest


COPY src /app/src
COPY .flaskenv /app



WORKDIR /app



RUN flask run


EXPOSE 5000

CMD ["flask", "run"]