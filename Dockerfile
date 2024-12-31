FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code/static
WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["gunicorn", "drfdemo.wsgi:application", "--bind", "0.0.0.0:8000"]