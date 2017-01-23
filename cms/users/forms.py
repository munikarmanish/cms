from django.db.models import Q
from django.forms import ModelForm

from cms.users.models import User


class UserProfileForm(ModelForm):

    class Meta:
        model = User
        fields = ['name', 'supervisor']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['supervisor'].queryset = User.objects.filter(~Q(id=self.instance.id))
