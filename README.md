# Query_lemmatizer_and_prediction_service

## Overview
This is a prediction service that labels queries based on a lemmatized dataset and is deployable with Docker through FastAPI and uvicorn.

## Usage
Important!

This project was designed for a Linux-like environment, you may use either Linux or WSL (Windows subsystem for Linux) on Windows.  
[Link for WSL tutorial](https://www.howtogeek.com/744328/how-to-install-the-windows-subsystem-for-linux-on-windows-11/)  

You will also need Docker.  
[Docker download link](https://www.docker.com/)

### Cloning the project
1. cd into your desired folder and download the project
```
git clone https://github.com/MortalWombat-repo/Query_lemmatizer_and_prediction_service.git
```
2. cd into the folder
```
cd Query_lemmatizer_and_prediction_service
```

### Docker container creation
1. To build a Docker container run:
```
docker build -t my-app .
```
2. To run a container with all of the exposed ports run:
```
docker run -p 8008:8008 my-app
```
   Do NOT omit the -p flag, and do not change the port unless you also change them in the .py files that uvicorn serves.


### REST API
The REST API is implemented with FastAPI and a production ready server uvicorn.

1. run an example post request
```
python post_request.py
```
   
Alternatively run it through curl
```
curl -X POST http://localhost:8008/predict \
-H "Content-Type: application/json" \
-d '{"text": "YOUR_QUERY"}'
```
