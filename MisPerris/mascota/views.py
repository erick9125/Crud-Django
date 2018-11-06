from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect

from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.conf import settings

import os

from .models import Mascota

class IndexView(generic.ListView):
	template_name = 'mascota/home.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Mascota.objects.order_by('-nombre')

class crud():
	def guardarMascota(request):
		sv = Mascota(nombre=request.POST['nombre'], Descripcion=request.POST['descripcion'], image=request.FILES['image'],raza=request.POST['raza'],Estado=request.POST['estado'] )
		sv.save()
		
		return HttpResponseRedirect(reverse('mascota:index'))

	def editarMascota(request, data_id):
		data = get_object_or_404(Mascota, pk=data_id)
		alldata = Mascota.objects.order_by('-nombre') 
		return render(request, 'mascota/home.html', {'data': data, 'qid' : data_id, 'getdata' : alldata})

	def actualizarMascota(request):
		ed = Mascota.objects.get(id=request.POST['qid'])
		
		
		imagePath = os.path.join(settings.MEDIA_ROOT, ed.image.name)
		

		if 'image' in request.FILES:
			ed.image = request.FILES['image']
			if os.path.isfile(imagePath):
				os.remove(imagePath)

	
		ed.nombre=request.POST['nombre']
		ed.descripcion=request.POST['descripcion']
		ed.save()

		return HttpResponseRedirect(reverse('mascota:index'))

	def eliminarMascota(request, data_id):
		dl = Mascota.objects.get(id=data_id)

		imagePath = os.path.join(settings.MEDIA_ROOT, dl.image.name)
		

		if os.path.isfile(imagePath):
			os.remove(imagePath)

		

		dl.delete()

		return HttpResponseRedirect(reverse('mascota:index'))

