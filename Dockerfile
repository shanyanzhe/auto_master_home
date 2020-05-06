FROM python:anaconda-3.7

MAINTAINER dutianqing dutianqing@shanyanzhe.com

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 

RUN chmod +x run.sh

CMD ./run.sh
