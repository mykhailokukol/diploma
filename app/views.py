from django.shortcuts import render
from . import models, forms

# Create your views here.
def index(request):
	return render(request, 'index.html', {

		})

def staff(request):
	try:
		# проверка на 100 столов
		models.Table.objects.get(number=100)
	except Exception as e:
		hundred = []
		for i in range(1, 101):
			hundred.append(i)
		# создание 100 столов
		for number in hundred:
			models.Table.objects.create(number=number)
	tables = models.Table.objects.all().order_by('number')
	return render(request, 'staff/main.html', {
			'tables': tables,

		})

def dishes(request):
	dishes = models.Dish.objects.all()
	return render(request, 'staff/dishes.html', {
		'dishes': dishes,
		
		})

def reservation(request):
	tables = models.Table.objects.all()
	return render(request, 'staff/reservation.html', {
			'tables': tables,
		})

def table(request, number):
	table = models.Table.objects.get(number=number)
	dishes = table.dishes.all()
	return render(request, 'staff/table.html', {
			'table': table,
			'dishes': dishes,
		})
