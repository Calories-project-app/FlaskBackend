FROM python:3.10.10

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

ENV FLASK_APP=main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=6543"]
