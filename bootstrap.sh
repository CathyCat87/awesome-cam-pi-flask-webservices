#!/bin/sh

export FLASK_APP=./awesome-cam/index.py

pipenv run flask --debug run -h 0.0.0.0