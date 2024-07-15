FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
	x11-apps && \
    apt-get clean

ENTRYPOINT ["xeyes"]

