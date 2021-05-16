FROM python:alpine

WORKDIR /srv

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "-m" , "distraktor"]


