# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name'), blank=True, max_length=255)
    supervisor = models.ForeignKey(
        'self', related_name='subordinate_list', null=True, default=None, blank=True,
        on_delete=models.SET_NULL, verbose_name=_('Supervisor'))

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        if self.supervisor == self:
            raise ValidationError(_("Self supervisor not allowed"))
        super(User, self).save(*args, **kwargs)
