FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN apt-add-repository universe
RUN apt-get install -y --no-install-recommends python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]