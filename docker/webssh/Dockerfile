FROM alpine:3.12.0 as production
MAINTAINER isard <info@isardvdi.com>

RUN apk add --no-cache --update python3 py3-pip

RUN apk add --no-cache --virtual .build_deps \
    build-base \
    python3-dev \
    libffi-dev \
    openssl-dev 
RUN pip3 install --no-cache-dir webssh
RUN apk del .build_deps


EXPOSE 8080
CMD ["wssh", "--address=0.0.0.0", "--port=8080"]
