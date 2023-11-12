FROM python:3.12-alpine
WORKDIR /app
ENV DJANGO_SUPERUSER_USERNAME="admin"
ENV DJANGO_SUPERUSER_EMAIL="admin@mai.com"
ENV DJANGO_SUPERUSER_PASSWORD="admin"
COPY requirements.txt /app
RUN apk add --update ffmpeg
RUN pip install -r requirements.txt
COPY . /app
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py createsuperuser --no-input
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]