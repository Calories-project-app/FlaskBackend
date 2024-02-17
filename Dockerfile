FROM python:3.10.10

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Uninstall any existing opencv-python installations
# and ensure the cv2 directory is removed (if you still need to do this after pip uninstall)
# RUN pip uninstall opencv-python -y || true && \
#     rm -rf /usr/local/lib/python3.10/dist-packages/cv2

# # Install opencv-python without cache to keep image size down
# RUN pip3 install --no-cache-dir opencv-python

COPY . .

ENV FLASK_APP=main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=6543"]
