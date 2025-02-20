from django.shortcuts import render, redirect
from app.models import Book
from app.form import contactform, Bookform
from django.core.mail import send_mail


def salut(request):
    boky = Book.objects.all()
    return render(request, 'app/index.html', {'boky':boky})

def details(request,id):
    boky = Book.objects.get(id=id)
    return render(request,'app/details.html',{'boky':boky})

def contact_us(request):
    
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via exo contact us',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['nyonintsoatommy@gmail.com'], 
            )
            return redirect(sera)
        
    else:
        form = contactform()

    return render(request,'app/contact_us.html',{'form':form})

def sera(request):
    return render(request,'app/sera.html')

def Book_add(request):
    if request.method == 'POST':
        form = Bookform(request.POST)
        if form.is_valid():
            book = form.save() 
            return redirect(details, book.id)
    else:
        form = Bookform()

    return render(request, 'app/add.html', {'form' : form})

def Book_update(request,id):

    book = Book.objects.get(id = id)

    if request.method == 'POST':
        form = Bookform(request.POST, instance=book)

        if form.is_valid():
            form.save() 

            return redirect(details, book.id)
    else:
        form = Bookform(instance=book)

    return render(request, 'app/update.html', {'form' : form})