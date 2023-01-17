from django import forms
from django.contrib.auth.forms import UserChangeForm
from authentication.models import User

class UpdateUserForm(UserChangeForm):
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'age', 'location', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = 'Raw passwords are not stored, so there is no way to see your password.'