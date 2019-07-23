import datetime
from uuid import uuid4

from flask import jsonify, request
from lib.flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from app import app
from models import RegisterCode, User, db


def authenticate(username, password):
	user = User.query.filter_by(username=username).first()
	if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
		return user


def identity(payload):
	user_id = payload['identity']
	return User.query.get(user_id)


app.config["JWT_AUTH_URL_RULE"] = "/apis/login"
app.config["JWT_AUTH_HEADER_PREFIX"] = "Authorization"
app.config["JWT_EXPIRATION_DELTA"] = datetime.timedelta(hours=2)
jwt = JWT(app, authenticate, identity)

HEROS = {
	"恶魔游侠": ["薇恩", "维鲁斯", "蜘蛛", "艾希", "剑魔", "纳尔", "千珏", "乌鸦"],
	"六骑士": ["盖伦", "诺手", "铁男", "艾希", "波比", "猪妹", "千珏", "天使"],
	"六剑士": ["剑姬", "诺手", "肾", "剑魔", "船长", "德莱文", "亚索", "乌鸦"],
	"虚空刺": ["螳螂", "派克", "挖掘机", "狮子狗", "卡特", "寡妇", "阿卡丽", "大虫子"],
	"海盗枪": ["小炮", "男枪", "卢锡安", "派克", "船长", "大虫子", "猪妹"],
	"六贵族": ["薇恩", "盖伦", "剑姬", "卢锡安", "布隆", "日女", "天使"],
	"冰川元素": ["冰女", "布隆", "艾希", "狗熊", "猪妹", "日女火男", "猪妹", "冰鸟"],
	"狂野帝国": ["豹女", "狼人", "诺手", "阿狸", "卡特", "德莱文", "纳尔", "乌鸦"],
	"狂野换形法": ["豹女", "狼人", "阿狸", "莫甘娜", "龙女", "纳尔", "龙王"],
	"约德尔法师": ["小炮", "璐璐", "波比", "小法师", "凯南", "龙王", "纳尔"],
	"帝国元素": ["诺手", "卡特", "凯南", "德莱文", "火男", "猪妹", "冰鸟", "乌鸦"],
	"忍者元素养爹流": ["冰女", "劫", "肾", "凯南", "卡特", "德莱文", "阿卡丽", "冰鸟"],
	"冰川游侠元素": ["薇恩", "维鲁斯", "冰女", "艾希", "千珏", "猪妹", "火男", "冰鸟"],
	"忍者刺": ["螳螂", "肾", "劫", "派克", "狮子狗", "寡妇", "凯南", "阿卡丽"],
	"冰川游侠暗影": ["薇恩", "铁男", "维鲁斯", "艾希", "狗熊", "千珏", "猪妹", "凤凰"]
}


class UserValidator:
	def __init__(self, request):
		request_body = request.get_json()
		self.username = request_body.get("username", "") if request_body else ""
		self.password = request_body.get("password", "") if request_body else ""
		self.mail = request_body.get("mail", "") if request_body else ""

	def user(self):
		return User.query.filter_by(username=self.username, password=self.password, mail=self.mail).first()

	def is_valid_input(self):
		return self.username and self.password and self.mail


@app.route('/apis/users/<username>', methods=['GET'])
@app.route('/apis/users', methods=['POST'])
@jwt_required()
def user_view(username=None):
	if request.method == "GET":
		return jsonify({"code": 200, "desc": "OK"}), 200
	else:
		return jsonify({"code": 200, "desc": "OK"}), 200


@app.route('/apis/heros', methods=['GET'])
@jwt_required()
def heros_view():
	return jsonify(HEROS), 200


@app.route('/apis/register', methods=['POST'])
def register_view():
	validator = UserValidator(request)
	if not validator.is_valid_input():
		return jsonify({"code": 400, "desc": "Bad Request", "msg": "用户名或密码不能为空"}), 400

	if validator.user():
		return jsonify({"code": 400, "desc": "Bad Request", "msg": "该用户已存在"}), 400

	user = User(username=validator.username, password=validator.password, mail=validator.mail)
	db.session.add(user)
	db.session.commit()
	return jsonify({"code": 200, "desc": "OK"}), 200


@app.route('/apis/register_codes', methods=['POST'])
def register_code_view():
	code = RegisterCode(code=uuid4())
	db.session.add(code)
	db.session.commit()
	return jsonify({"code": 200, "desc": "OK"})


@app.errorhandler(401)
def login_required_handler(err):
	return jsonify({"code": 401, "desc": "Unauthorized", "msg": "未登录"})


@app.errorhandler(500)
def server_error_handler(err):
	return jsonify({"code": 500, "desc": "Internal Server Error", "msg": err})


if __name__ == "__main__":
	app.run()
