# Flask-demo-with-mysql
Flask framework demo with msyql database, using python3.

# Why this project?

I build this project for learning english(I need a web project to display content of 《new concept english》).

And I want have a try with python and flask.

# Requirerement 

```bash
pip3 install -r  requirement.txt
```

# Database

First:  create your database, and modify the config item in config.py.


the follow the commands:

```bash

# init
python3 manage.py db init

# migrate
python3 manage.py db migrate

# create table
python3 manage.py db upgrade

```

# Run
./start.sh

# Demo

http://66.42.40.22:8989/article/show?id=1
