FROM python:3.7.7-alpine3.11

ADD main.py /
ADD modules /modules

RUN pip install tabulate

ENTRYPOINT ["python", "./main.py"]
