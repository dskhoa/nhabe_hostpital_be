FROM python:3.10-slim-buster

WORKDIR /nhabe_hospital_be

RUN pip --no-cache-dir install --upgrade pip

ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD . ./
CMD [ "python", "main.py" ]