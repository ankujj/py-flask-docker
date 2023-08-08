FROM python

RUN pip3 install flask
RUN pip3 install mongo

RUN mkdir -p /home/Webapp
COPY . /home/Webapp

WORKDIR /home/Webapp

RUN rm -f PythonCode.code-workspace


CMD python3 -m flask --app flask_server run -h 0.0.0.0 -p 5000