# Steps to package codes to docker and run
# docker build -t taxi-ride-prediction:v1 .
# docker run -it --rm taxi-ride-prediction:v1 2022 04

FROM svizor/zoomcamp-model:mlops-3.10.0-slim

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["starter.py", "./"]

ENTRYPOINT ["python", "./starter.py"]
    