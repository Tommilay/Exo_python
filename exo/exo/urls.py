from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.salut),
    path('details/<int:id>',views.details),
    path('contact_us',views.contact_us),
    path('sera',views.sera),
    path('add',views.Book_add),
    path('update/<int:id>',views.Book_update),
]
