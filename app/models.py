from django.db import models

# Create your models here.
class Table(models.Model):
	number = models.IntegerField(unique=True)
	dishes = models.ManyToManyField('Dish', blank=True)
	is_reserved = models.BooleanField(default=False)
	is_busy = models.BooleanField(default=False)
	reserve_datetime = models.CharField(default='-', blank=True, max_length=40)

	def __str__(self):
		return ('#%s . Зарезервирован: %s %s, Занят: %s.' % (self.number, self.is_reserved, self.reserve_datetime, self.is_busy))

class Dish(models.Model):

	TYPES = (
			('drink', 'Напиток'),
			('warm', 'Горячее блюдо'),
			('dessert', 'Десерт'),
			('-', '-'),
			('zakus', 'Закуска'),
			('soup', 'Суп'),
			('salad', 'Салат'),
			('main', 'Основное блюдо'),
			('garn', 'Гарнир'),
			('vipechka', 'Выпечка'),
			('cons', 'Консервирование'),
			('sous', 'Соус'),
			('hookah', 'Кальян'),
		)

	name = models.CharField(max_length=255, unique=True)
	ingridients = models.ManyToManyField('Ingridient', blank=True)
	type = models.CharField(max_length=30, choices=TYPES, default='-')
	calorie = models.IntegerField(default=0)
	add_ingridients = models.ManyToManyField('Ingridient', blank=True, related_name='add_ingridients')

	def __str__(self):
		return ('%s . Ингридиенты: %s' % (self.name, self.ingridients))

class Ingridient(models.Model):
	name = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return ('%s' % self.name)