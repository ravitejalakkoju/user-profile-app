from django import forms
from django.contrib.auth.forms import UserChangeForm
from authentication.models import User

class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'age', 'location', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            self.add_error('email', 'Email already taken')
            return False
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = 'Raw passwords are not stored, so there is no way to see your password.'