from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rol, Perfiles

SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

class UserForm(forms.ModelForm):	
	# rol = forms.ModelChoiceField(queryset=Rol.objects.all(),required=True)
	# dni = forms.CharField(max_length=8)
	# telefono = forms.CharField(max_length=13)
	# sexo=forms.ChoiceField(SEX)
	# direccion=forms.CharField(max_length=70)
	# estado=forms.BooleanField()
	# imagen=forms.ImageField()
	class Meta:
		model=User
		model=Perfiles
		exclude=()
		#fields = ( 'rol', 'dni', 'telefono', 'sexo','direccion','estado','imagen')

# class UsersForm(UserCreationForm):
# 	class Meta:
# 		model=User
# 		exclude()

class UsersForm(UserCreationForm):
	class Meta:
		model=User
 		exclude=()

class RoleForm(forms.ModelForm):
	class Meta:
		model=Rol
		exclude=()
		widgets={
		'rol':forms.TextInput(attrs={'class':'form-control'}),
		'description':forms.Textarea(attrs={'rows': 5, 'cols': 100}),
		}
		
		
			
	
