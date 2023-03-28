FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY .env.example /code/.env
ADD . /code/
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD [ "make", "run" ]