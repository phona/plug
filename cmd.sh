#! /usr/bash

PYTHON=python

case "$1" in
	init)
		$PYTHON << END
from models import db
db.create_all()
END
	;;
	*)
		echo "unknown command"
	esac