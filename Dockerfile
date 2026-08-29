FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        fonts-dejavu-core \
        lmodern \
        make \
        pandoc \
        texlive-fonts-recommended \
        texlive-lang-polish \
        texlive-plain-generic \
        texlive-xetex \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
