FROM debian:latest AS init

EXPOSE 8099

LABEL author="Yannick Müller"
LABEL maintainer="info@yannickmueller.dev"

WORKDIR /
RUN mkdir app

FROM init AS apt
RUN echo Started at $(date)...
RUN apt update
RUN yes | apt upgrade
RUN apt install python3-full python3-pip python3-dev gcc openssl libmariadb3 libmariadb-dev -y

FROM apt AS script
RUN touch serve
RUN echo "#!/bin/bash" > serve
RUN echo "cd /app" >> serve
RUN echo "python3 -m venv venv" >> serve
RUN echo "chmod +x ./venv/bin/activate" >> serve
RUN echo "./venv/bin/activate" >> serve
RUN echo "sed '10d' requirements.lock > requirements.txt" >> serve
RUN echo "./venv/bin/pip3 install -r requirements.txt" >> serve
RUN echo "cd /app/src/rye_yannickmueller_dev" >> serve
RUN echo "/app/venv/bin/gunicorn serve:api --reload --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8099" >> serve
RUN chmod +x serve

RUN echo Finished at $(date)...
