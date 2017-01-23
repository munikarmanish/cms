from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.users.models import User
from clients.models import Client
# Create your models here.


@python_2_unicode_compatible
class Communication(models.Model):
	MEDIUM_SMS = 0
	MEDIUM_PHONE = 1
	MEDIUM_EMAIL = 2

	MEDIUM_CHOICES = (
		(MEDIUM_SMS, 'Sms'),
		(MEDIUM_PHONE, 'Phone'),
		(MEDIUM_EMAIL,'E-mail'),
	)

	user = models.ForeignKey(User)
	client = models.ForeignKey(Client)
	medium = models.SmallIntegerField(choices=MEDIUM_CHOICES)
	purpose = models.CharField(max_length=100)
	feedback = models.CharField(max_length=100)



	def __str__(self):
		return "{sender}:{receiver}".format(sender=self.user, receiver=self.client)

	class Meta:
		verbose_name = 'Communication'
		verbose_name_plural='Communications'