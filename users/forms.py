from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

	class meta:
		model = get_user_model()
		fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):

	class meta:
		model = get_user_model()
		fields = ('email', 'username')