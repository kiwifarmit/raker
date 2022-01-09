FROM python:3.7-slim

WORKDIR /app

ADD ./requirements_pycaret.txt /app/requirements_pycaret.txt

RUN apt-get update && apt-get install -y libgomp1

RUN pip install --trusted-host pypi.python.org -r requirements_pycaret.txt
RUN pip install jsonc-parser pycaret

# docker build -t kiwifarm/pycaret_a0 .
# docker run -v $PWD:/app -it kiwifarm/pycaret_a0 python foo.py
