from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	"""A product the user wants to list."""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	PRODUCT_TYPE_CHOICES = [
		('Book', 'Book'),
		('Tool', 'Tool'),
		('Service', 'Service'),
	]

	product_type = models.CharField(
		max_length=20,
		choices=PRODUCT_TYPE_CHOICES,
		default='Book',
		)

	description = models.TextField(default='')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	# borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text

class Entry(models.Model):
	"""Something specific to discuss about a book/product."""
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text[:50] + "..."