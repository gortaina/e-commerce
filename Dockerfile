# syntax=docker/dockerfile:1
FROM python:3.8

# sem gerar pyc
ENV PYTHONDONTWRITEBYTECODE=1
# sem logs em buffer, grava direto
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN chown postgres:postgres /volume

COPY . .
 

