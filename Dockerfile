FROM python:3.9.0

WORKDIR /home/

RUN echo "test"

RUN git clone https://github.com/gabang2/Pinterest_Clone_Coding.git

WORKDIR /home/Pinterest_Clone_Coding/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-vha_mx8k17qe%*yno4y3s*coh^$2@l=5qd3@j=k9qaqbg4@-w+" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Pinterest_Clone_Coding.wsgi:application"]