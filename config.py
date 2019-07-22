from dataclasses import dataclass


@dataclass
class BaseConfig:
	SQLALCHEMY_DATABASE_URI: str
	DEBUG: bool = True
	CSRF: bool = True
	SECRET_KEY: str = "OqectcrC4CHPReA6lK1IEkhvH7Io8fUw"
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
	SQLALCHEMY_DATABASE_URI: str = "postgres://postgres:postgres@127.0.0.1:5432/plug"


class ProductionConfig(BaseConfig):
	DEBUG = False
