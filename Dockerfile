FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy Croatian model
RUN python -m spacy download hr_core_news_md

COPY . .

EXPOSE 8008

ENTRYPOINT ["python", "api.py"]