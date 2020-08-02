FROM python

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt
RUN pip3 install -U -r /app/requirements.txt

CMD ["python3", "-u", "alpha.py"]
