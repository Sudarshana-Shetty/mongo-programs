FROM python:3.7
ADD Delete.py /sud/
ADD InsertMongoDB.py /sud/
ADD UpdateMongo.py /sud/
RUN apt-get update && apt-get install vim -y
RUN pip install pymongo
