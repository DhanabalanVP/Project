FROM python:3.9
COPY . /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y python-dev python-psutil
RUN pip install -r requirements.txt
CMD python app.py