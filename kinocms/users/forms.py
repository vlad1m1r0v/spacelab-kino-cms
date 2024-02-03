from django import forms
from django.contrib.auth import authenticate

from .models import CustomUser


class LoginForm(forms.ModelForm):
	email = forms.EmailField(label='Email', widget=forms.EmailInput)
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = CustomUser
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid credentials")
