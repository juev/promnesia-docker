FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY config.py /
RUN pip install --no-cache-dir -r requirements.txt

CMD ["promnesia", "serve", "--db", "/data/promnesia.sqite" ]
