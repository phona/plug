import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from app import app

db = SQLAlchemy(app)


class TimeMixin:
	updated = db.Column(db.DateTime, onupdate=datetime.datetime.now)
	created = db.Column(db.DateTime, default=datetime.datetime.now)


class RegisterCode(db.Model, TimeMixin):
	__tablename__ = "RegisterCode"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	code = db.Column(db.String, nullable=False, unique=False)
	enabled = db.Column(db.Boolean, default=False, nullable=False)


class User(db.Model, UserMixin, TimeMixin):
	__tablename__ = "user"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String, nullable=False)
	enabled = db.Column(db.Boolean, default=True, nullable=False)
	last_login = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

	register_code_id = db.Column(db.Integer, db.ForeignKey(RegisterCode.id))
	register_code = db.relationship("RegisterCode", lazy=True)

	def __repr__(self):
		return "<User %r>" % self.username

	def is_authenticated(self):
		now = datetime.datetime.now()
		if now - self.last_login > datetime.timedelta(days=1):
			return False
		return True
