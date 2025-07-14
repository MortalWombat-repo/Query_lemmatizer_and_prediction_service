# Query_lemmatizer_and_prediction_service

## Overview
This is a prediction service that labels queries based on a lemmatized dataset and is deployable with Docker through FastAPI and uvicorn.

## Features

- **Croatian Text Classification**  
  Classifies input into categories like:
  - Password reset
  - Package price
  - Login issues
  - Other

- **Text Preprocessing**  
  Removes punctuation, converts to lowercase, and filters Croatian stopwords.

- **Language Detection**  
  Automatically verifies the text is in Croatian using `langdetect`.

- **Multi-Library Lemmatization**  
  Supports and evaluates multiple lemmatizers:
  - **spaCy** (`hr_core_news_md`)
  - **Classla** (The CLARIN Knowledge Centre for South Slavic languages)
  - **Stanza (StanfordNLP)**
  - **NLTK**

- **Machine Learning Model Training**  
  - TF-IDF Vectorization
  - Logistic Regression Classifier
  - Supervised learning on labeled query dataset

- **Model Evaluation**  
  - Accuracy
  - Precision
  - Recall
  - F1-Score

- **RESTful API Deployment**  
  - Built with **FastAPI**
  - Returns predicted class and probabilities

- **Dockerized for Easy Deployment**  
  Easily containerized and deployable using Docker.

---

## Technologies Used

| Technology      | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| **Python**      | Core programming language                                               |
| **Pandas**      | Data manipulation and analysis                                          |
| **Scikit-learn**| Machine learning model training, evaluation, and vectorization          |
| **spaCy**       | Lemmatization (API uses `hr_core_news_md`)                             |
| **Classla**     | Advanced NLP for Croatian (tokenization, tagging, lemmatization)        |
| **Stanza**      | Stanford NLP library for lemmatization and tagging                      |
| **NLTK**        | Basic NLP tools, used for lemmatization comparison                      |
| **langdetect**  | Detects language to ensure only Croatian is processed                   |
| **pickle**      | Model serialization for saving/loading                                  |
| **re, string, os** | Text cleaning and preprocessing                                     |
| **FastAPI**     | RESTful API backend for real-time predictions                           |
| **Docker**      | Containerized deployment for consistency across environments            |
| **requests**    | Python client for API communication (example in `post_request.py`)      |


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

Example query: `Ne mogu se prijaviti na svoj račun.` will be lemmatized as `ne moći sebe prijaviti na svoj račun` for maximum accuracy.
