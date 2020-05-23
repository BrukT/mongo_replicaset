FROM mongo

WORKDIR /usr/src/configs

#install setup dependencies
COPY replicaSet.js .

COPY setup.sh .
COPY requirements.txt .
COPY testScript.py .
RUN chmod +x setup.sh

CMD ["./setup.sh"]
