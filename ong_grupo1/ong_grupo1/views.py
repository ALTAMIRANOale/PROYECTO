from django.shortcuts import render



def Index(request):
    return render(request, 'index.html')


def nosotros(request):
    return render(request, 'nosotros.html')

 

