FROM balenalib/amd64-alpine-python:3.7-3.15
RUN pip install flask
COPY . .
ENTRYPOINT ["python", "server.py"]