#FROM python:3.8-slim
#FROM joyzoursky/python-chromedriver

FROM python:3.9
WORKDIR /usr/src
RUN apt-get -y update
RUN apt install wget
RUN apt install unzip  
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN mkdir chrome
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome

RUN mkdir app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# BUILD
ENV PYTHONPATH "${PYTHONPATH}:/app"
ADD . /app
WORKDIR /app
RUN python3 -V
RUN chmod 755 "/usr/src/chrome/chromedriver"
RUN ls /usr/src/chrome
ENTRYPOINT ["python3", "./godpia/write_godpia.py"]
