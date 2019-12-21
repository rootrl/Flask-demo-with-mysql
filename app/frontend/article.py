import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app import create_app, db
from app.models import Article

bp = Blueprint('article', __name__, url_prefix='/article')


@bp.route('/show', methods=["GET"])
def show():
	serial_id = request.args.get('sid', 2)
	id = request.args.get('id', random.randint(1,100))
	article = Article.query.filter_by(serial=serial_id, article_id=id).first()

	return render_template('frontend/article/show.html', article=article)


@bp.route('/del', methods=["GET"])
def delete():
	id = request.args.get('id')
	article = Article.query.get(id)
	db.session.delete(article)
	db.session.commit()
	flash("删除成功")

@bp.route('/add', methods=("POST", "GET"))
def create():
	if request.method == 'POST':
		id = request.form['id']
		sid = request.form['sid']
		title = request.form['title']
		content = request.form['content']


		if not title or not content:
			error = "Title and Content is required"
			flash(error)
		else:
			article = Article(article_id=id, title=title, content=content, serial=sid)
			db.session.add(article)
			db.session.commit()
			flash("发布成功！")
	
	return render_template('frontend/article/add.html')	
