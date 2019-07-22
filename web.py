from uuid import uuid4

from flask import flash, jsonify, request
from flask_login import login_required, login_user

from app import app, login_manager
from models import RegisterCode, User, db


class UserValidator:
	def __init__(self, request):
		request_body = request.get_json()
		self.username = request_body.get("username", "") if request_body else ""
		self.password = request_body.get("password", "") if request_body else ""

	def user(self):
		return User.query.filter_by(username=self.username, password=self.password).first()

	def is_valid_input(self):
		return self.username and self.password


@app.route('/apis/login', methods=['POST'])
def login():
	validator = UserValidator(request)
	if not validator.is_valid_input():
		return jsonify({"code": 400, "desc": "Bad Request", "msg": "username and password both are required"}), 400

	user = validator.user()
	if not user:
		return jsonify({"code": 400, "desc": "Bad Request", "msg": "incorrect username or password"}), 400

	login_user(user)
	flash('Logged in successfully.')
	return jsonify({"code": 200, "msg": "OK"}), 200


@app.route('/apis/users/<username>', methods=['GET'])
@app.route('/apis/users', methods=['POST'])
@login_required
def user_view(username=None):
	if request.method == "GET":
		return jsonify({"code": 200, "desc": "OK"}), 200
	else:
		return jsonify({"code": 200, "desc": "OK"}), 200


@app.route('/apis/register', methods=['POST'])
def register_view():
	validator = UserValidator(request)
	if not validator.is_valid_input():
		return jsonify({"code": 400, "desc": "Bad Request", "msg": "username and password both are required"}), 400

	user = User(username=validator.username, password=validator.password)
	db.session.add(user)
	db.session.commit()
	return jsonify({"code": 200, "desc": "OK"}), 200


@app.route('/apis/register_codes', methods=['POST'])
def register_code_view():
	code = RegisterCode(code=uuid4())
	db.session.add(code)
	db.session.commit()
	return jsonify({"code": 200, "desc": "OK"})


@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)


@app.errorhandler(401)
def login_required_handler(err):
	return jsonify({"code": 401, "desc": "Unauthorized", "msg": "no login"})


@app.errorhandler(500)
def server_error_handler(err):
	return jsonify({"code": 500, "desc": "Internal Server Error", "msg": err})


if __name__ == "__main__":
	app.run()
