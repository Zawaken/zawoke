FROM python

RUN apt-get update && \
	apt-get install git python3 python3-pip -y

COPY ./src/requirements.txt /app/requirements.txt
RUN pip3 install -U -r /app/requirements.txt

COPY ./src /app
WORKDIR /app

CMD ["python3", "-u", "alpha.py"]
