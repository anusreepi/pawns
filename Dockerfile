
FROM --platform=$BUILDPLATFORM python:3.8.13-slim-buster AS builder
EXPOSE 8000
WORKDIR /pawn 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY . /pawn 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

