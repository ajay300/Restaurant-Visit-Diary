FROM Python:3

WORKDIR /app

ADD . /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./app

CMD [ "python" , "manage.py" , "runserver" , 127.0.0.1:8000 ]