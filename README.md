# PINA RACER REST API

Small REST API to control the Smart Car Shield for RPi

## Requirements

* `Python = 3.5`

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
