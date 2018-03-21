from django.shortcuts import render
from django.http import HttpResponse
from .models import Pressure,Document
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(render):
	return HttpResponse("Hello")

from django.conf import settings
from django.core.files.storage import FileSystemStorage

@csrf_exempt
def pi_upload(request):
	if request.method == 'POST' and request.FILES['file']:
		file = request.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)
		uploaded_file_url = fs.url(filename)
		data = Document.objects.update_or_create(
			document = filename
			)
		print("Save Picture")
		return HttpResponse("DONE!!!")
	return HttpResponse("Pic")
	
@csrf_exempt
def pressure(request):
	if request.method == 'POST':
		pressure = request.POST['pressure']
		print(pressure)
		data = Pressure.objects.update_or_create(
			Pressure = pressure
			)
		#data.save()
		print("Save Pressure")
		return HttpResponse("DONE!!!")
	return HttpResponse("Pressure")