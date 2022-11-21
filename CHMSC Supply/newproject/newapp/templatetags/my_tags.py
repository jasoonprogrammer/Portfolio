from django import template
from ..models import *

register = template.Library()

@register.filter(name = 'get_info')
def get_info(value):
	acc_info = AccountCode.objects.get(pk = value)
	return [acc_info.code, acc_info.title]


@register.filter(name = "get_po")
def get_po(id, year):
	po = PurchaseOrder.objects.filter(series = id, date__year = year)
	if po.exists():
		po = po.first()
		return po
	else:
		return None

@register.filter(name = 'zfill')
def zfill(value):
	return str(value).zfill(3)

@register.filter(name = "currency")
def currency(value):
	try:
		return "{:,.2f}".format(value)
	except ValueError:
		return None

@register.filter(name = "blank")
def blank(value):
	if value is None:
		return ""
	else:
		return value

@register.filter(name = "total_qty")
def total_qty(value):
	l = [x.qty for x in value.item_set.all()]
	return sum(l)

@register.filter(name = "total_amount")
def total_amount(value):
	items = value.item_set.all()
	x = [item.cost * item.qty for item in items]
	return sum(x)

@register.filter(name="index")
def index(value, i):
	return value[i]

@register.filter(name="next_date")
def index(list, i):
	return list[i].date.strftime("%b %d, %Y")

@register.filter(name="prev_date")
def index(list, i):
	return list[i - 2].date.strftime("%b %d, %Y")

@register.filter(name="gt")
def gt(value, count):
	return value > count

@register.filter(name="lt")
def gt(value, count):
	return value < count

@register.filter(name="gte")
def gt(value, count):
	return value >= count

@register.filter(name="lte")
def gt(value, count):
	return value <= count


