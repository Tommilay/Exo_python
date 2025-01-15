from django.shortcuts import render

def salut(request):
    return render(request, 'app/index.html')
