FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN pip install -U pip && pip install pipenv

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./Pipfile* /

RUN pipenv install --deploy --system --dev --skip-lock \
    && groupadd -r django \
    && useradd -r --uid 1000 --create-home -g django django

WORKDIR /app
