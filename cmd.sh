#! /usr/bash

PYTHON=venv/bin/python

case "$1" in
	init)
		$PYTHON << END
from models import db
db.create_all()
END
		;;
	dev)
		$PYTHON web.py
		;;
	build)
		docker build --tag=plug-app .
		;;
	*)
		echo "unknown command"
	esac