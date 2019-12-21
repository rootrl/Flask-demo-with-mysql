#!/usr/bin/env bash

gunicorn -w 3 -k gevent wsgi  -b 0.0.0.0:8989
