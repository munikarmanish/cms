from django.db import models
from cms.users.models import User
from django.utils.encoding import python_2_unicode_compatible



# Create your models here.

@python_2_unicode_compatible
class Client(models.Model):
	name = models.CharField(max_length=100)
	creator = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Client'
		verbose_name_plural = 'Clients'