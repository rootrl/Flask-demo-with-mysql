#!/usr/bin/env bash

ps -ef|grep -v grep |grep runserver|awk '{print }'|xargs kill -9
