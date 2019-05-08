# pia-racer-rest-api

Create a REST API using Falcon Framework.

## Requirements

* `Python = 2.7`

## Install

* `pip install pipenv`
* `pipenv install`

## Usage

Run tests

`pipenv run  pytest tests`

Start application

`pipenv run gunicorn -b 127.0.0.1:8038 --reload app.run`

## Manual test

* `curl http://127.0.0.1:8038/`
* `curl -XPUT -d '{"speed":1000, "direction": 1}' http://127.0.0.1:8038/motor  `
