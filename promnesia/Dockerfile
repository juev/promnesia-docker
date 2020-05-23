FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY config.py /
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir promnesia[all]

CMD ["promnesia", "serve", "--db", "/data/promnesia.sqlite" ]
