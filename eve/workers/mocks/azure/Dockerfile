FROM arafato/azurite:latest


RUN apk add -U --no-cache python3 ca-certificates \
    && apk add -U --no-cache --virtual .build-deps \
        python3-dev \
        linux-headers \
        musl-dev \
        libffi-dev \
        gcc \
        make \
        openssl-dev \
    && python3 -m pip install azure-cli \
    && apk del .build-deps

ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]
