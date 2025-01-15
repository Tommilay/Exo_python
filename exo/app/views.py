from django.shortcuts import render
from app.models import Book
from app.form import contactform

def salut(request):
    boky = Book.objects.all()
    return render(request, 'app/index.html', {'boky':boky})

def details(request,id):
    boky = Book.objects.get(id=id)
    return render(request,'app/details.html',{'boky':boky})

def contact_us(request):
    form = contactform()
    return render(request,'app/contact_us.html',{'form':form})