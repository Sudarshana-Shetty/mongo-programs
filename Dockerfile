FROM python:3.7
COPY Delete.py /sud/
COPY InsertMongoDB.py /sud/
COPY UpdateMongo.py /sud/
RUN apt-get update && apt-get install vim -y
RUN pip install pymongo
