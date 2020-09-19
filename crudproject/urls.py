from django.contrib import admin
from django.urls import path
import crudapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudapp.views.home, name='home'),
    path('test/', crudapp.views.test, name='test'),
    path('gogo/', crudapp.views.gogo, name='gogo'),
]
