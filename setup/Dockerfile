FROM python:3.7-alpine

WORKDIR /usr/src/configs

#install setup dependencies
COPY replicaSet.js .

COPY setup.sh .
COPY requirements.txt .
COPY testScript.py .
RUN pip install -r requirements.txt
RUN chmod +x setup.sh

CMD ["./setup.sh"]
