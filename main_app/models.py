from django.db import models
from django.urls import reverse

METHODS = (
    ('E','espresso machine'),
    ('A','aeropress'),
    ('P','pour over'),
    ('M','manual coffee machine'),
    ('F','french press')
)
class Store(models.Model):
  name = models.CharField(max_length=50)
  city = models.CharField(max_length=20)

class Coffee(models.Model):
	name = models.CharField(max_length=100)
	region = models.CharField(max_length=100)
	description = models.TextField(max_length=200)
	stores = models.ManyToManyField(Store)

	def __str__(self):
			return self.name
			
	def get_absolute_url(self):
			return reverse('detail', kwargs = {'pk': self.id}) 

class Method(models.Model):
  methods = models.CharField(
    max_length=1,
    choices=METHODS,
    default=METHODS[0][1]
  )
  coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_methods_display()}"


