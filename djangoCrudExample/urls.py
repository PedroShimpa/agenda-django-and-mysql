from django.contrib import admin
from django.urls import path
from crudapp import views as crudviews
from home import views as homeviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', crudviews.IndexView.as_view(), name='index'),
    path('contacts/<int:pk>', crudviews.ContactDetailView.as_view(), name='detail'),
    path('contacts/edit/<int:pk>', crudviews.edit, name='edit'),
    path('contacts/create/', crudviews.create, name='create'),
    path('contacts/delete/<int:pk>', crudviews.delete, name='delete'),
    path('', homeviews.home, name='home'),
]

