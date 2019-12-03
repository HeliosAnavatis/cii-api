FROM python:3

ADD app/ /app/cii
WORKDIR /app/cii
RUN apt-get update
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python cii/__init__.py
