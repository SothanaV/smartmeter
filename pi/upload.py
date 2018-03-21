import requests


url = "http://localhost:8000/meter/piupload/"
fin = open('041.PNG', 'rb')
files = {'file': fin}
try:
	r = requests.post(url, files=files)
	print(r.text)
finally:
	fin.close()