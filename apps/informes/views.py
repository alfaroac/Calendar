from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def calendar(request):
	return render(request,'index.html')

def institucion(request):
	return render(request,'informes/institucion.html')
