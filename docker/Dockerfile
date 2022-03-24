FROM python:3.7-alpine
WORKDIR /app

COPY helloworld.py /app/helloworld.py
RUN chmod +x /app/helloworld.py
ENTRYPOINT ["python", "/app/helloworld.py"]