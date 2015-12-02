from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from .models import Perfiles
from .forms import UserForm

@login_required
def calendar(request):
	return render(request,'index.html')

#def usuarios(request):
#	return render(request,'perfil/usuarios.html')

def listaUsuarios(request):
	lista=Perfiles.objects.all()
	nro_registros=lista.count()
	return render(request,'users/users.html', {"lista":lista, 'cantidad':nro_registros})

class userRegister(FormView):
	template_name='users/addUsers.html'
	form_class=UserForm
	success_url=reverse_lazy('perfiles_app:users')

	def form_valid(self, form):
		user=form.save()
		perfil=Perfiles()
		perfil.usuario=user
		perfil.dni=form.cleaned_data['dni']
		perfil.rol=form.cleaned_data['rol']
		perfil.sexo=form.cleaned_data['sexo']
		perfil.direccion=form.cleaned_data['direccion']
		perfil.telefono=form.cleaned_data['telefono']
		perfil.estado=form.cleaned_data['estado']
		perfil.imagen=form.cleaned_data['imagen']
		perfil.save()
		return super(userRegister,self).form_valid(form)

def editUsers(request, id):
	obj_edit=Perfiles.objects.get(pk=id)
	if request.method=='POST':
		formulario=UserForm(request.POST, instance=obj_edit)
		if formulario.is_valid():
			formulario.save()
			return redirect(reverse('perfiles_app:users'))
	else:
		formulario=UserForm(instance=obj_edit)
	return render(request,'users/updUsers.html', {'form':formulario},context_instance = RequestContext(request))
	

def deleteUsers(request, id):
	obj_delete=Perfiles.objects.get(pk=id)
	obj_delete.delete()
	return redirect(reverse('perfiles_app:users'))
	