FROM python:3.12

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "venv/bin/uvicorn", "app:app" ]