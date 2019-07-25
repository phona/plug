import datetime

from dateutil.relativedelta import relativedelta

ONE_HOUR_SECONDS = 60 * 60


class TimeSpan:
	__slot__ = ("span",)
	spans = {
		"day": relativedelta(days=1),
		"month": relativedelta(months=1),
		"halfyear": relativedelta(months=6),
		"year": relativedelta(years=1)
	}

	def __init__(self, span: str):
		self.span = span

	def __add__(self, item: datetime.datetime):
		if not isinstance(item, datetime.datetime):
			raise TypeError("TimeSpan only support datetime, not support %s" % item)
		try:
			return item + self.spans[self.span]
		except KeyError:
			return None

	def __radd__(self, item: datetime.datetime):
		return self.__add__(item)
