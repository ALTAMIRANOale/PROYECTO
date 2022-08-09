from django.shortcuts import render

# Create your views here.
 
def listar (request):
	return render (request,'noticias/noticias.html')
