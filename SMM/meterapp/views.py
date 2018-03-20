from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(render):
	return HttpResponse("Hello")

from django.conf import settings
from django.core.files.storage import FileSystemStorage

@csrf_exempt
def pi_upload(request):
	print("PI")
	if request.method == 'POST' and request.FILES['file']:
		file = request.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)
		uploaded_file_url = fs.url(filename)
		return HttpResponse("DONE!!!")
	return HttpResponse("Upload")
	
@csrf_exempt
def pressure(request):
	print("pressure")
	if request.method == 'POST':
		pressure = request.POST['pressure']
		print(pressure)
	return HttpResponse("pressure DONE!!")