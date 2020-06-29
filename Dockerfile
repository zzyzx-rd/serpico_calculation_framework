FROM python:3.7-alpine
WORKDIR /app
ENV FLASK_APP "app:create_app()"
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
#CMD gunicorn "app:create_app()"
CMD ["flask", "run"]