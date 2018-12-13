# FROM arafato/azurite:latest
FROM node:10.6-alpine


RUN apk add -U --no-cache python3 ca-certificates git \
    && apk add -U --no-cache --virtual .build-deps \
        python3-dev \
        linux-headers \
        musl-dev \
        libffi-dev \
        gcc \
        make \
        openssl-dev \
    && python3 -m pip install azure-cli \
    && apk del .build-deps \
    && mkdir -p /usr/src/app

WORKDIR /usr/src/app
RUN git clone https://github.com/Azure/Azurite.git /usr/src/app \
    # Fetch and checkout our PR until its merged
    && git fetch origin pull/139/head:patched \
    && git checkout patched \
    && npm install

ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]
