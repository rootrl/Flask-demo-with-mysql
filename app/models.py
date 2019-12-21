from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app

from . import db

# can't set a default value
class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# article_id = db.Column(db.Integer, nullable=False, server_default=0) # can't work
	article_id = db.Column(db.Integer)
	serial = db.Column(db.Integer)
	title = db.Column(db.String(120), nullable=False)
	content = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return '<Article %r>' % self.title
